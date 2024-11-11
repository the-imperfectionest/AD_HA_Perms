from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

DOMAIN = "ad_ha_perms"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the AD HA Permissions component."""
    # You can set up the config and initiate the sensor
    hass.data[DOMAIN] = "Active Directory Permissions Integration"

    # Create and register a sensor
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {}, config)
    return True
