from rest_framework.filters import BaseFilterBackend

from core.serializers import StockFilterSerializer


class StockFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        serializer = StockFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if x := data.get('name'):
            queryset = queryset.filter(name__icontains=x)

        if x := data.get('ticker'):
            queryset = queryset.filter(ticker__icontains=x)

        return queryset
