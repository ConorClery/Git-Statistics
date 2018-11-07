# importing the requests library
import requests
import sys

github = 'https://api.github.com/'
user = ''
pw = ''
user = input('Enter in Github username (or skip for limited querires): ')
if user != '':
    pw = input('Enter in Github password: ')

print('Number of endpoints to query = ', (len(sys.argv) - 1))
for i, endpoint in enumerate(sys.argv):
    if i > 0:
        print('\nURL', i, ': ', github, endpoint)
        URL = github + endpoint
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'Content-Type':'application/json'}
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS, auth =( user, pw ))
        print(r.status_code)
        print(r.headers)
        contentType = r.headers['Content-Type'].split(';')
        if contentType[0] == 'application/json':
            data = r.json()
            print('Recieved data', data)
