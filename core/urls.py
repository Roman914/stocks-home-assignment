from rest_framework.routers import DefaultRouter

# from core.views import StockView, StockDailyDataView
from core.views import StockView

router = DefaultRouter()

router.register('stocks', StockView, basename='stocks')
# router.register('stocksock_daily_data', StockDailyDataView, basename='stock_daily_data')

urlpatterns = router.urls
