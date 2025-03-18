# from unittest import mock

# from django.test import TestCase

# from ingest.strategies.cc.serializers.html.business_html_serializer import BusinessHTMLSerializer
# from ingest.strategies.cc.models import BusinessProductPage

# class BusinessCCSerializerTestCase(TestCase):
#     """Django TestCase for BusinessHTMLSerializer."""

#     @mock.patch('requests.Session.get')
#     def test_serializer(self, mock_get):
#         """Test the serializer with HTML."""
        
#         with open('/app/lib/cc/tests/fixture_data/bcc_product_page.html') as f:
#             mock_response = mock_get.return_value
#             mock_response.text = f.read()

#             # Initialize the serializer and BusinessProductPage instance
#             serializer = BusinessHTMLSerializer()
#             business_product_page = BusinessProductPage(123)

#             # Serialize the data and test the output
#             inventory = serializer.serialize(business_product_page)
#             self.assertEqual(inventory.name, "ASUS TUF Gaming GeForce RTX 5090 32GB GDDR7 AI Gaming Graphics Card TUF-RTX5090-32G-GAMING")
#             self.assertEqual(inventory.id, 123)
#             self.assertEqual(inventory.locations[0].name, "Head Office")
#             self.assertEqual(inventory.locations[0].stock, 0)

#     def test_expected_failure(self):
#         """This test is expected to fail."""
#         self.assertFalse(True)  # Simulate failure