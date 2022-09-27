from django.utils import timezone
from rest_framework import serializers as rfs

from core.models import Stock, StockDailyData


class StockSerializer0(rfs.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'name',
            'ticker',
        )


class StockDailyDataSerializer(rfs.ModelSerializer):
    class Meta:
        model = StockDailyData
        fields = (
            'stock',
            'date',
            'open',
            'close',
            'high',
            'low',
            'volume',
        )


class StockSerializer1(rfs.ModelSerializer):
    recent_daily_data = rfs.SerializerMethodField(read_only=True)

    class Meta:
        model = Stock
        fields = (
            'id',
            'name',
            'ticker',
            'recent_daily_data',
        )

    @staticmethod
    def get_recent_daily_data(stock):
        recent_daily_data = stock.daily_data.filter(
            date__gte=timezone.now() - timezone.timedelta(days=10)
        )
        return StockDailyDataSerializer(recent_daily_data, many=True).data


# noinspection PyAbstractClass
class StockFilterSerializer(rfs.Serializer):
    search = rfs.CharField(required=False)


# noinspection PyAbstractClass
class StockDailyDataFilterSerializer(rfs.Serializer):
    service_available = rfs.BooleanField(default=True)



