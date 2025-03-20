from rest_framework import serializers

from tracking.models import ItemStock


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStock
        fields = '__all__'
