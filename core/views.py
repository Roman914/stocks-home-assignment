from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.filters import StockFilter
from core.models import Stock, StockDailyData
from core.serializers import StockSerializer0, StockSerializer1, StockDailyDataFilterSerializer
from yahoo_fin import stock_info
import pandas as pd


class StockView(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    serializer_class = StockSerializer0
    filter_backends = (StockFilter,)
    queryset = Stock.objects.all()

    @staticmethod
    def transform_daily_data(daily_data_res: pd.DataFrame):
        daily_data_res.drop(columns=['ticker', 'adjclose'], inplace=True)
        return daily_data_res.to_dict(orient='records')

    @staticmethod
    def save_daily_data_to_db(instance, data):
        objects_to_create = [
            StockDailyData(stock=instance, **i) for i in data
        ]
        return StockDailyData.objects.bulk_create(
            objects_to_create,
            batch_size=1000,
            ignore_conflicts=True
        )

    @method_decorator(cache_page(60*15))
    @action(methods=['get'], detail=True)
    def daily_data(self, request, pk):
        instance = self.get_object()
        today = timezone.now().today()

        serializer = StockDailyDataFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data
        service_available = params.get('service_available')

        try:
            """ bring ticker's data from our source """
            last_two_weeks_daily_data = stock_info.get_data(
                instance.ticker,
                start_date=today - timezone.timedelta(days=10),
                end_date=today,
                index_as_date=False,
                interval="1d"
                )
        except Exception as e:
            """ in case of any unexpected server error - since we depends here on third party source"""
            last_two_weeks_daily_data = pd.DataFrame()

        if not last_two_weeks_daily_data.empty and service_available:
            last_two_weeks_daily_data_transformed = self.transform_daily_data(last_two_weeks_daily_data)
            self.save_daily_data_to_db(instance, last_two_weeks_daily_data_transformed)
        serializer = StockSerializer1(instance)
        return Response(serializer.data)
