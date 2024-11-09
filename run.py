import json
import requests
from ldap3 import Server, Connection

AD_SERVER = "ldap://your-ad-server"
USERNAME = "your-ad-username"
PASSWORD = "your-ad-password"
BASE_DN = "DC=your,DC=domain,DC=com"
HA_URL = "http://supervisor/core/api"
HA_TOKEN = "your-ha-access-token"

def query_active_directory():
    server = Server(AD_SERVER, get_info="ALL")
    conn = Connection(server, USERNAME, PASSWORD, auto_bind=True)
    conn.search(BASE_DN, "(objectClass=user)", attributes=["sAMAccountName", "displayName", "nfcTag", "kioskLocation", "lightControl"])

    users = []
    for entry in conn.entries:
        users.append({
            "username": entry.sAMAccountName.value,
            "display_name": entry.displayName.value,
            "nfc_tag": entry.nfcTag.value,
            "kiosk_location": entry.kioskLocation.value,
            "light_control": entry.lightControl.value
        })
    return users

def update_home_assistant(users):
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"users": users}
    response = requests.post(f"{HA_URL}/states/sensor.ad_user_permissions", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Successfully updated Home Assistant with AD permissions.")
    else:
        print(f"Failed to update Home Assistant: {response.status_code}")

if __name__ == "__main__":
    users = query_active_directory()
    update_home_assistant(users)
