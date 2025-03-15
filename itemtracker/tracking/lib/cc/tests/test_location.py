import pytest

from lib.cc.factories.location_factory import LocationFactory
from lib.cc.models.location import Location


class TestLocation:
    """Generic pytest class template."""

    @classmethod
    def setup_class(cls):
        """Runs once before any tests in the class."""
        cls.factory = LocationFactory()

    @classmethod
    def teardown_class(cls):
        """Runs once after all tests in the class."""
        del cls.factory

    def test_create_location(self):
        """Example test case 1."""
        location = self.factory.create("location1", 42)
        assert isinstance(location, Location)
        assert location.name == "location1"
        assert location.stock == 42

    @pytest.mark.xfail(reason="This test is expected to fail")
    def test_expected_failure(self):
        """This test is expected to fail."""
        assert False