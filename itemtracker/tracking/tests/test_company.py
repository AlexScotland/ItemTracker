from django.test import TestCase

from tracking.factories import CompanyFactory
from tracking.models import Company


class InventoryTestCase(TestCase):
    """Django TestCase for Company model."""

    @classmethod
    def setUpTestData(cls):
        """Runs once before any test methods."""
        cls.factory = CompanyFactory

    def test_company_creation(self):
        """Test if the factory creates a valid company."""
        sample_company = self.factory.create(name="company1")  # Fixed factory call
        sample_company.save()
        self.assertIsInstance(sample_company, Company)
        self.assertEqual(sample_company.name, "company1")
        self.assertIsNotNone(sample_company.id)
