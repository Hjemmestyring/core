"""Define fixtures available for all tests."""
from unittest.mock import MagicMock, patch

from canary.api import Api
from pytest import fixture


@fixture
def canary(hass):
    """Mock the CanaryApi for easier testing."""
    with patch.object(Api, "login", return_value=True), patch(
        "homeassistant.components.canary.Api"
    ) as mock_canary:
        instance = mock_canary.return_value = Api(
            "test-username",
            "test-password",
            1,
        )

        instance.login = MagicMock(return_value=True)
        instance.get_entries = MagicMock(return_value=[])
        instance.get_locations = MagicMock(return_value=[])
        instance.get_location = MagicMock(return_value=None)
        instance.get_modes = MagicMock(return_value=[])
        instance.get_readings = MagicMock(return_value=[])
        instance.get_latest_readings = MagicMock(return_value=[])
        instance.set_location_mode = MagicMock(return_value=None)

        yield mock_canary