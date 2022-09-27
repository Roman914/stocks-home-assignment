from django.contrib import admin

from core.models import Stock, StockDailyData


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'ticker',
        'updated_at',
        'created_at',
    )
    fields = (
        'name',
        'ticker',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'name',
        'ticker',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )


@admin.register(StockDailyData)
class StockDailyDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'stock',
        'open',
        'close',
        'high',
        'low',
        'volume',
    )
    fields = (
        'date',
        'stock',
        'open',
        'close',
        'high',
        'low',
        'volume',
        'updated_at',
        'created_at',
    )
    search_fields = (
        'stock__ticker',
        'stock__name',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
    )
