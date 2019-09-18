# -*- coding: utf-8 -*-

import base64
import getpass
import json
import requests

'''
This script demonstrates basic PI Web API interaction with the data archive 
by creating a point, carrying out several options on it, and then deleting it.
2. POST: Create a PI Point.
3. GET: The PI Point by query string.
4. GET: The PI Point by WebID.
5. PATCH: Modify an attribute of the PI Point.
6. POST: Add a value to the created PI Point.
7. GET: The latest recorded value of the created PI Point.
8. DELETE: The created PI Point.
'''

# Server info
webapi_url = 'https://52.173.141.236/piwebapi'
dataserver_name = 'RADIXUSPISRVR'
dataserver_webid = 's0o2nFwRTcEk241JW-ymYf2QUkFESVhVU1BJU1JWUg'
point_webid = None # Will be created later

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

point_data = {
    "Name": "TEST.WebAPI",
    "Descriptor": "Test PI Point created via PI Web API",
    "PointClass": "classic",
    "PointType": "Float32",
    "EngineeringUnits": "",
    "Step": False,
    "Future": False
}

# Disable ssl cert warnings
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

# 1.
def create_pi_point (webapi_url, dataserver_webid, headers, point_data):
    
    url = r'{}/dataservers/{}/points'.format(webapi_url, dataserver_webid)
    
    r = requests.post(
        url,
        headers=headers,
        data=json.dumps(point_data),
        verify=False
    )

    r.raise_for_status()
    return r

# 2.
def get_pi_point_by_path (webapi_url, dataserver_name, headers, point_data):
    
    url = r'{}/points'.format(webapi_url)
    
    r = requests.get(
         url,
         headers=headers,
         params = {"path": r"\\RADIXUSPISRVR\TEST.WebAPI"},
         verify=False
    )    
    
    r.raise_for_status()
    return json.loads(r.content)["WebId"]   

# 4.
def get_pi_point_by_webid (webapi_url, headers, point_webid):
    
    url = r'{}/points/{}'.format(webapi_url, point_webid)

    r = requests.get(
        url,
        headers=headers,
        verify=False
    )
    
    r.raise_for_status()
    return r

# 8.
def delete_pi_point(webapi_url, headers, point_webid):
    
    url = r'{}/points/{}'.format(webapi_url, point_webid)

    r = requests.delete(
        url,
        headers=headers,
        verify=False
    )
    
    r.raise_for_status()
    return r

create_pi_point(webapi_url, dataserver_webid, headers, point_data)
point_webid = get_pi_point_by_path (webapi_url, dataserver_name, headers, point_data)
get_pi_point_by_webid (webapi_url, headers, point_webid)

delete_pi_point(webapi_url, headers, point_webid)