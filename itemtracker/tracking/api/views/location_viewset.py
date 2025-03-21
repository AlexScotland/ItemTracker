from rest_framework import viewsets

from tracking.models import Location
from tracking.api.serializers.location_serializer import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
