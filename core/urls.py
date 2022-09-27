from rest_framework.routers import DefaultRouter

from core.views import StockView

router = DefaultRouter()

router.register('stocks', StockView, basename='stocks')

urlpatterns = router.urls
