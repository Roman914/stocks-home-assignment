import os.path

from django.core.management import BaseCommand
from django.db import transaction as t
import json

from core.models import Stock
from stocks.settings.base import BASE_DIR


class Command(BaseCommand):
    help = 'Create initial Data.'

    @t.atomic()
    def handle(self, *args, **options):
        self.load_data()
        self.stdout.write('Success.')

    @staticmethod
    def load_data():
        data_path = os.path.join(BASE_DIR.parent, 'core', 'symbols_data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)

        stocks_to_create = []
        tickers_list = list(Stock.objects.values_list('ticker', flat=True))
        for i in data:
            if not i['Ticker'] in tickers_list:
                stocks_to_create.append(
                    Stock(
                        name=i['Name'],
                        ticker=i['Ticker'],
                    )
                )
        Stock.objects.bulk_create(stocks_to_create, batch_size=1000)
