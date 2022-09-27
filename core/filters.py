from rest_framework.filters import BaseFilterBackend
from django.db.models import Q

from core.serializers import StockFilterSerializer


class StockFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        serializer = StockFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if x := data.get('search'):
            queryset = queryset.filter(
                Q(name__icontains=x) |
                Q(ticker__icontains=x)
            )

        return queryset
