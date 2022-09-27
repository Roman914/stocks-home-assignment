from common.models import CreatedUpdatedAtMixin
from django.db import models


class Stock(CreatedUpdatedAtMixin):
    name = models.CharField(unique=True, max_length=64)
    ticker = models.CharField(unique=True, max_length=4)

    def __str__(self):
        return self.ticker


class StockDailyData(CreatedUpdatedAtMixin):
    date = models.DateField()
    stock = models.ForeignKey(
        'core.Stock',
        on_delete=models.CASCADE,
        related_name='daily_data',
    )
    open = models.DecimalField(max_digits=10, decimal_places=5)
    close = models.DecimalField(max_digits=10, decimal_places=5)
    high = models.DecimalField(max_digits=10, decimal_places=5)
    low = models.DecimalField(max_digits=10, decimal_places=5)
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('stock', 'date')

    def __str__(self):
        return f'{self.date} {self.stock.ticker}'
