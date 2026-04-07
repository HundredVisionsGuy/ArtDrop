"""
controller.py
by HundredVisionsguy
Does all the work behind the scenes.
"""

import requests as re
import json

# Build out the URL based on the API and endpoints
collections_base_api = "https://api.artic.edu/api/v1/"
search_term = "monet"
artworks_search = collections_base_api + "artworks/search?q=" + search_term

# try and make a call
response = re.get(artworks_search)
result = ""
if response.ok:
    result = response.text
    try:
        # try to convert from json string to a dictionary or string
        result = json.loads(result)
    except Exception as ex:
        result = ex
else:
    result = f"Error: {response.status_code} - Reason: {response.reason}"
for key in result.keys():
    print(key)

# Get info
data = result.get("data")
print(data)