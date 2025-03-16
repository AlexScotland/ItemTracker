from django.test import TestCase

from tracking.factories import LocationFactory, CompanyFactory
from tracking.models import Location, Company


class LocationTestCase(TestCase):
    """Django TestCase for Location model."""

    @classmethod
    def setUpTestData(cls):
        """Runs once before any test methods."""
        cls.factory = LocationFactory()
        cls.company = CompanyFactory.create(name="company1")
        cls.company.save()

    def test_create_location(self):
        """Test creating a location with a generated UUID."""
        location = self.factory.create(name="location1", company=self.company, external_id="1234")
        location.save()
        self.assertIsInstance(location, Location)
        self.assertEqual(location.name, "location1")
        self.assertEqual(location.company, self.company)
        self.assertEqual(isinstance(location.company, Company), True)
        self.assertEqual(location.external_id, "1234")
        self.assertIsNotNone(location.id)
