import requests
import sys
import getpass
import json
from firebase import firebase

firebaseEndpoint = 'https://swengdb.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebaseEndpoint, None)
github = 'https://api.github.com/'
user = ''
pw = ''
dataObj = {}

def processRepoData( data ):
    dataLength = len(data["items"])
    print("Current Data Progress: 0/", dataLength)
    for element in data["items"]:
        numOut = 0
        num = 0
        repUrl = element["repos_url"]
        repoData = getRepoData( repUrl )
        repoLength = len(repoData)
        print("Posting data from", repoLength, "repositories...")
        print("Current User Progress: 0/", repoLength)
        for repo in repoData:
            getAndPostRepoLanguageData(repo["owner"]["login"], repo["name"])
            num = num + 1
            woops = str(num) + '/' + str(repoLength)
            print("Current User Progress:", woops)
        numOut = numOut + 1
        noops = str(numOut) + "/" + str(dataLength)
        print("Current Data Progress:", noops)
    return

def getRepoData( repUrl ):
    PARAMS = {'Content-Type':'application/json'}
    r = requests.get(url = repUrl, params = PARAMS, auth =( user, pw ))
    return r.json()

def getAndPostRepoLanguageData(owner, name):
    langUrl = github + 'repos/' + owner + '/' + name +'/languages'
    PARAMS = {'Content-Type':'application/json'}
    r = requests.get(url = langUrl, params = PARAMS, auth =( user, pw ))
    object = r.json()
    checkIfLangInArrayAndConstruct(dataObj, object)
    return

def checkIfLangInArrayAndConstruct(arr, obj):
    for (k, v) in obj.items():
       print("Key: " + k)
       print("Value: " + str(v))
       if containsLang(dataObj, k) is False:
           dataObj[k] = v
           #Insert key into json obj and set value
       if containsLang(dataObj, k) is True:
           dataObj[k] = dataObj[k] + v
           #Find key and add to value

def containsLang(obj, key):
    if key in obj:
        return True
    return False

user = input('Enter in Github username (or skip for limited querires): ')
if user != '':
    pw = getpass.getpass('Enter in Github password: ')

print('Number of endpoints to query = ', (len(sys.argv) - 1), '\nBeginning given requests...\n')
for i, endpoint in enumerate(sys.argv):
    if i > 0:
        URL = github + endpoint
        print('\nURL', i, ': ', URL)
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'Content-Type':'application/json'}
        # sending get request and saving the response as response object
        j = 0
        limit = 1
        prog = ''
        while j < limit:
            prog = str(j) + '/' + str(limit)
            print('Overall Progress:', prog)
            page = '&page=' + str(j)
            r = requests.get(url = URL + (page), params = PARAMS, auth =( user, pw ))
            print(r.status_code)
            contentType = r.headers['Content-Type'].split(';')
            if contentType[0] == 'application/json':
                data = r.json()
                #print('Recieved data: ', json.dumps(data, sort_keys=True, indent=4))
                processRepoData(data)
            j = j + 1
            prog = str(limit) + '/' + str(limit)
        print(dataObj)
        print("Posting shcraped data to db...")
        fireData = {'progLangs' : r.json(), 'owner': owner, 'repo_name' : name }
        sent = json.dumps(fireData)
        result = firebase.post("/languageData", sent)
print("Done!")
