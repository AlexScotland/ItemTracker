from rest_framework.routers import DefaultRouter

from tracking.api.views import ItemStockViewset, CompanyViewSet, LocationViewSet, ItemViewSet

MAIN_ROUTER = DefaultRouter()

MAIN_ROUTER.register(r'stock', ItemStockViewset, basename='stock-watch')
MAIN_ROUTER.register(r'companies', CompanyViewSet, basename='company')
MAIN_ROUTER.register(r'locations', LocationViewSet, basename='location')
MAIN_ROUTER.register(r'items', ItemViewSet, basename='item')
