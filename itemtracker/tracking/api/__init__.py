from rest_framework.routers import DefaultRouter

from tracking.api.views import ItemStockViewset

MAIN_ROUTER = DefaultRouter()

MAIN_ROUTER.register(r'stock', ItemStockViewset, basename='stock-watch')
