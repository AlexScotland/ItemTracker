from unittest import mock

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from tracking.models import ItemStock, Location, Item, Company
from ingest.strategies.cc.models import BusinessProductPage

class UpdateStockViaAPITestCase(TestCase):
    """Django TestCase for Updating Stock via the API."""

    def setUp(self):
        """Set up the test case with initial data."""
        self.client = APIClient()
        self.company = Company.objects.create(name='Canada Computers Business')
        self.company.save()
        self.item = Item.objects.create(
            name='ASUS TUF Gaming GeForce RTX 5090 32GB GDDR7 AI Gaming Graphics Card TUF-RTX5090-32G-GAMING',
            company=self.company,
            external_id=123
        )
        self.item.save()
        self.location = Location.objects.create(
            name='Head Office',
            external_id= None,
            company=self.company
        )
        self.location.save()
        self.item_stock = ItemStock.objects.create(item=self.item, location=self.location, stock=10)
        self.item_stock.save()

    @mock.patch('requests.Session.get')
    def test_serializer(self, mock_get):
        """Test the serializer with HTML."""

        with open('/app/itemtracker/ingest/strategies/cc/tests/fixture_data/bcc_product_page.html') as f:
            mock_response = mock_get.return_value
            mock_response.text = f.read()

            self.client.post(
                reverse('check-stock'),{
                    'company': self.item.company.id,
                    'item': self.item.id
                    }
                )
            self.assertEqual(ItemStock.objects.get(id=self.item_stock.id).stock, 0)
