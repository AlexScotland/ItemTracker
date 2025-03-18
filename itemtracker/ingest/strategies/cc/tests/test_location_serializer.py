from unittest import mock

from django.test import TestCase

from ingest.strategies.cc.serializers.html.business_html_serializer import BusinessHTMLSerializer
from ingest.strategies.cc.models import BusinessProductPage

class BusinessCCLocationSerializerTestCase(TestCase):
    """Django TestCase for BusinessHTMLSerializer."""

    @mock.patch('requests.Session.get')
    def test_serializer(self, mock_get):
        """Test the serializer with HTML."""

        with open('/app/itemtracker/ingest/strategies/cc/tests/fixture_data/bcc_product_page.html') as f:
            mock_response = mock_get.return_value
            mock_response.text = f.read()

            # Initialize the serializer and BusinessProductPage instance
            serializer = BusinessHTMLSerializer(BusinessProductPage(123))

            # Serialize the data and test the output
            locations = serializer.serialize()
            self.assertEqual(location.name, "Head Office")
