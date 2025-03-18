from django.test import TestCase

from tracking.factories import InventoryFactory, CompanyFactory, LocationFactory, ItemFactory
from tracking.models import ItemStock


class InventoryTestCase(TestCase):
    """Django TestCase for Company model."""

    @classmethod
    def setUpTestData(cls):
        """Runs once before any test methods."""
        cls.factory = InventoryFactory
        cls.company = CompanyFactory.create(name="company1")
        cls.company.save()
        cls.location = LocationFactory.create(name="location1", company=cls.company, external_id="1234")
        cls.location.save()
        cls.item = ItemFactory.create(name="item1", url="url", external_id="123", location=cls.location)
        cls.item.save()

    def test_company_creation(self):
        """Test if the factory creates a valid company."""
        sample_inventory = self.factory.create(location=self.location, item=self.item, stock=10)
        sample_inventory.save()
        self.assertIsInstance(sample_inventory, ItemStock)
        self.assertEqual(sample_inventory.stock, 10)
        self.assertIsNotNone(sample_inventory.id)
        self.assertEqual(sample_inventory.location, self.location)
        self.assertEqual(sample_inventory.item, self.item)
