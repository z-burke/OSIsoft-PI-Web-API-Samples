import base64
import getpass
import json
import requests

# Get User credentials
UN = 'DOMAIN\USERNAME'
PW = "PASSWORD"

FQDN = "PI_WEB_API_SERVER_FQDN"
WEBID = "POINT_WEBID"

# Convert user credentials to auth header
auth_string = '%s:%s' % (UN, PW)
auth_base64 = base64.b64encode(str.encode(auth_string))
auth = 'Basic %s' % (auth_base64.decode())

# Generate request headers
headers = {
            'Authorization': auth,
            'Content-Type': 'application/json',
            "X-Requested-With":"message/http",
        }


value_data = {
        "Value": 991,
} # Because no time stamp is specified, PI Web API will add value at current time.

# Make request
r = requests.post(
    f'https://{FQDN}/piwebapi/streams/{WEBID}/value',
    headers=headers,
    data=json.dumps(value_data),
    verify=False
)

# If request was successful, convert response to json object.
if r.status_code == 200:
    response_body = json.loads(r.content)
    