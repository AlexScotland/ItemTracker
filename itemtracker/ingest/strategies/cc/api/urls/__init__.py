from django.urls import path
from ingest.strategies.cc.api.views import CheckStock

urlpatterns = [
    path('update/', CheckStock.as_view(), name='check-stock'),
]