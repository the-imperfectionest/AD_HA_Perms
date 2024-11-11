import logging
from ldap3 import Server, Connection, ALL
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ad_ha_perms"

class ADPermsSensor(Entity):
    """Representation of a Sensor that queries Active Directory (AD) for permissions"""

    def __init__(self, host, user, password):
        """Initialize the sensor."""
        self._host = host
        self._user = user
        self._password = password
        self._state = None
        self._connection = None

    def _connect_ldap(self):
        """Connect to the Active Directory server."""
        server = Server(self._host, get_info=ALL)
        self._connection = Connection(server, user=self._user, password=self._password)
        return self._connection.bind()

    def update(self):
        """Update the state from Active Directory."""
        if self._connection is None or not self._connection.bound:
            if not self._connect_ldap():
                _LOGGER.error("Unable to connect to AD server.")
                return
        # Example query: search for a specific DN or entry
        self._connection.search(
            'dc=example,dc=com',
            '(objectClass=person)',
            attributes=['cn', 'sn', 'memberOf']
        )
        if self._connection.entries:
            # Example: return the CN of the first entry
            self._state = self._connection.entries[0].cn.value

    @property
    def name(self):
        """Return the name of the sensor."""
        return "AD Permissions Sensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
