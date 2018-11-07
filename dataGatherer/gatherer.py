# importing the requests library
import requests
import sys

print('Number of endpoints to query = ', (len(sys.argv) - 1))
for i, endpoint in enumerate(sys.argv):
    if i > 0:
        print("URL:", i, endpoint)

#for endpoint in sys.argv
# api-endpoint
URL = "http://www.google.ie"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location,
          'Content-Type':'application/json'}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

print(r.status_code)
print(r.headers)
if r.headers['Content-Type'] == 'application/json':
    data = r.json()
