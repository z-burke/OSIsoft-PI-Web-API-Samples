import base64
import getpass
import requests

# Get user credentials
UN = 'DOMAIN\USERNAME'
PW = "PASSWORD"

# Server info
FQDN = "PI_WEB_API_SERVER_FQDN"
WEBID = "POINT_WEBID"

# Convert user credentials to auth header
auth_string = '%s:%s' % (UN, PW)
auth_base64 = base64.b64encode(str.encode(auth_string))
auth = 'Basic %s' % (auth_base64.decode())

# Generate request headers
headers = {
            'Authorization': auth
        }

# Make request
r = requests.get(f'https://{FQDN}/piwebapi/points/{WEBID}', headers=headers, verify=False) # Set verify=False to allow bad dev SSL cert.

# If request was successful, convert response to json object.
if r.status_code == 200:
    response_body = r.json
