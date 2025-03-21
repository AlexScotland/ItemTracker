from rest_framework import viewsets

from tracking.models import Company
from tracking.api.serializers.company_serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing companies.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
