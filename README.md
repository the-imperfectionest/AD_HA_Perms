# Active Directory Permissions Add-on for Home Assistant

This add-on queries your Active Directory for user attributes like NFC tags and room/location permissions, then posts them to Home Assistant for use in automations and UI restrictions.

### Usage

1. Configure your Active Directory server and credentials in `config.json`.
2. Run the add-on; it will create a Home Assistant sensor `sensor.ad_user_permissions` with AD user permissions.
3. Use the sensor data to restrict access to lights, dashboards, or automations!

### License

Licensed under the Beerware License (Revision 42). If you find it useful, consider buying the author a beer if you ever meet them!
