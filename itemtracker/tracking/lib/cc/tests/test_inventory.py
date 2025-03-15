import pytest

from lib.cc.factories.inventory_factory import InventoryFactory
from lib.cc.factories.location_factory import LocationFactory
from lib.cc.models.inventory import Inventory

class TestInventory:
    """Generic pytest class template."""

    @classmethod
    def setup_class(cls):
        """Runs once before any tests in the class."""
        cls.location_factory = LocationFactory()
        cls.inventory_factory = InventoryFactory()

    @classmethod
    def teardown_class(cls):
        """Runs once after all tests in the class."""
        del cls.factory

    def test_create_location_and_inventory(self):
        """This testcase tests the generic factory"""
        location = [self.location_factory.create("location1", 42)]
        inventory = self.inventory_factory.create(123, "inventory1", location)
        assert isinstance(inventory, Inventory)
        assert inventory.id == 123
        assert inventory.name == "inventory1"
        assert inventory.locations == location

    @pytest.mark.xfail(reason="This test is expected to fail")
    def test_expected_failure(self):
        """This test is expected to fail."""
        assert False