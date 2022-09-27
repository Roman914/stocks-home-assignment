import os

from django.core.asgi import get_asgi_application
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'stocks.settings.{config("DJANGO_ENV")}')

application = get_asgi_application()
