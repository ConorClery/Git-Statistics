# importing the requests library
import requests
import sys
import getpass
import json
from firebase import firebase


def processData( data ):
    print(data["bio"])
    str = data["bio"]
    str = str.lower()
    if "student" and "trinity" and "dublin" in str:
        return True


github = 'https://api.github.com/'
user = ''
pw = ''
user = input('Enter in Github username (or skip for limited querires): ')
if user != '':
    pw = getpass.getpass('Enter in Github password: ')

print('Number of endpoints to query = ', (len(sys.argv) - 1), '\nBeginning given requests...\n')
for i, endpoint in enumerate(sys.argv):
    if i > 0:
        print('\nURL', i, ': ', github, endpoint)
        URL = github + endpoint
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'Content-Type':'application/json'}
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS, auth =( user, pw ))
        print(r.status_code)
        #print(r.headers)
        contentType = r.headers['Content-Type'].split(';')
        if contentType[0] == 'application/json':
            data = r.json()
            if processData(data) is True:
                print("Tis true!")
                #langdata = getUserStats(data)
                #postToFirebase(langdata)
            #print('Recieved data: ', json.dumps(data, sort_keys=True, indent=4))

#firebase = firebase.FirebaseApplication('https://swengdb.firebaseio.com/', None)
#result = firebase.get('/users', None)
#print(result)
