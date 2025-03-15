from django.test import TestCase

from tracking.factories import ItemFactory, CompanyFactory, LocationFactory
from tracking.models import Item, Company, Location


class ItemTestCase(TestCase):
    """Django TestCase for Item model."""

    @classmethod
    def setUpTestData(cls):
        """Runs once before any test methods."""
        cls.factory = CompanyFactory
        cls.company = CompanyFactory.create(name="company1")
        cls.company.save()
        cls.location = LocationFactory.create(name="location1", company=cls.company, external_id="1234")
        cls.location.save()

    def test_item_creation(self):
        """Test if the factory creates a valid item."""
        test_item = ItemFactory.create(
                                name="item1",
                                external_id="1234",
                                url="http://example.com",
                                stock=10,
                                location=self.location)
        test_item.save()
        self.assertEqual(test_item.name, "item1")
        self.assertEqual(test_item.external_id, "1234")
        self.assertEqual(test_item.url, "http://example.com")
        self.assertEqual(test_item.stock, 10)
        self.assertEqual(test_item.location, self.location)
