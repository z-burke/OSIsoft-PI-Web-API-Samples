import base64
import getpass
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
            'Authorization': auth
        }

# Make request
r = requests.get('https://52.173.141.236/piwebapi/points/P0o2nFwRTcEk241JW-ymYf2QSx0AAAUkFESVhVU1BJU1JWUlwxOUFHMjAwMQ', headers=headers, verify=False)

# If request was successful, convert response to json object.
if r.status_code == 200:
    response_body = r.json
