from rest_framework import viewsets

from tracking.models import Item
from tracking.api.serializers.item_serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for Item table.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
