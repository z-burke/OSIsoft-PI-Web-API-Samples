import base64
import getpass
import json
import requests

# Get User credentials
un = 'radixus\zachary.burke'
pw = None

# Convert user credentials to auth header
auth_string = '%s:%s' % (un, pw)
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
}

### Make request
#dataserver_webId = 's0o2nFwRTcEk241JW-ymYf2QUkFESVhVU1BJU1JWUg'
r = requests.post(
    'https://52.173.141.236/piwebapi/streams/P0o2nFwRTcEk241JW-ymYf2QIyIAAAUkFESVhVU1BJU1JWUlxURVNULldFQkFQSS5aQg/value',
    headers=headers,
    data=json.dumps(value_data),
    verify=False
)

# If request was successful, convert response to json object.
if r.status_code == 200:
    response_body = json.loads(r.content)
    