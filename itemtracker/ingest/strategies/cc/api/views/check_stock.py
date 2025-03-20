from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from tracking.api.serializers.inventory_serializer import InventorySerializer
from tracking.models import ItemStock
from ingest.strategies.cc.serializers.html.business_html_serializer import BusinessHTMLSerializer
from ingest.strategies.cc.models import BusinessProductPage


class CheckStock(CreateAPIView):
    queryset = ItemStock.objects.all()
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        # Fetch the ItemStock object based on the item ID from the request
        try:
            item_stock = ItemStock.objects.get(item=request.data.get('item'))
        except ItemStock.DoesNotExist:
            return Response(
                {"error": "ItemStock not found for the given item."},
                status=status.HTTP_404_NOT_FOUND
            )

        BusinessHTMLSerializer(BusinessProductPage(item_stock.item.external_id)).serialize()

        return Response(
            {"message": "Stock updated successfully."},
            status=status.HTTP_200_OK
        )
    