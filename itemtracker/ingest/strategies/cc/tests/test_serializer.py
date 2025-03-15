# import pytest
# from unittest import mock

# from lib.cc.serializers.html.business_html_serializer import BusinessHTMLSerializer
# from lib.cc.wrappers.business_product_page import BusinessProductPage

# class TestBusinessCCSerializer:
#     """Generic pytest class template."""

#     @classmethod
#     def setup_class(cls):
#         """Runs once before any tests in the class."""
#         cls.serializer = BusinessHTMLSerializer()

#     @classmethod
#     def teardown_class(cls):
#         """Runs once after all tests in the class."""
#         del cls.factory

#     @mock.patch('requests.Session.get')
#     def test_serializer(self, mock_get):
#         """This tests the factory with html"""
        
#         with open('/app/lib/cc/tests/fixture_data/bcc_product_page.html') as f:
#             mock_response = mock_get.return_value
#             mock_response.text = f.read()
#             serializer = BusinessHTMLSerializer()
#             business_product_page = BusinessProductPage(123)
#             inventory = serializer.serialize(business_product_page)
#             assert inventory.name == "ASUS TUF Gaming GeForce RTX 5090 32GB GDDR7 AI Gaming Graphics Card TUF-RTX5090-32G-GAMING"
#             assert inventory.id == 123
#             assert inventory.locations[0].name == "Head Office"
#             assert inventory.locations[0].stock == 0

#     @pytest.mark.xfail(reason="This test is expected to fail")
#     def test_expected_failure(self):
#         """This test is expected to fail."""
#         assert False