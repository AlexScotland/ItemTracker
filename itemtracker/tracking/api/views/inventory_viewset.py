from rest_framework import viewsets

from tracking.models import ItemStock
from tracking.api.serializers.inventory_serializer import InventorySerializer


class ItemStockViewset(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = ItemStock.objects.all()
    serializer_class = InventorySerializer
