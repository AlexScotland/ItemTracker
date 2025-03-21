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

            # Check Global Stock Pre Update
            response = self.client.get(reverse('stock-watch-list'))
            self.assertEqual(response.data[0]['stock'], 10)

            self.client.post(
                reverse('check-stock'), {
                    'company': self.item.company.id,
                    'item': self.item.id
                    }
                )
            self.assertEqual(ItemStock.objects.get(id=self.item_stock.id).stock, 0)

            # Check Global Stock for Update
            response = self.client.get(reverse('stock-watch-list'))
            self.assertEqual(response.data[0]['stock'], 0)

    def test_itemstock_not_found(self):
        """Test failure when ItemStock does not exist."""
        # Provide an invalid item ID that does not exist
        response = self.client.post(
            reverse('check-stock'),
            data={'company': self.company.id, 'item': 9999},  # Non-existent item ID
            format='json'
        )

        # Assert that the response returns a 404 status
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'ItemStock not found for the given item.')

    def test_missing_required_fields(self):
        """Test failure when required fields are missing."""
        # Omit the 'item' field in the request data
        response = self.client.post(
            reverse('check-stock'),
            data={'company': self.company.id},  # Missing 'item'
            format='json'
        )

        # Assert that the response returns a 400 status
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('item', response.data.get('error'))

    def test_invalid_data(self):
        """Test failure when invalid data is provided."""
        # Provide invalid data for the 'item' field
        response = self.client.post(
            reverse('check-stock'),
            data={'company': self.company.id, 'item': '2bf0282e-fa19-4420-ad95-b1aea3d21120' },  # Invalid item ID (string instead of integer)
            format='json'
        )

        # Assert that the response returns a 400 status
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('item', response.data.get('error'))