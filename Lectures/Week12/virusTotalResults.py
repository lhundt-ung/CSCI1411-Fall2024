import requests
import json

apiKey = '<API KEY>'
resource = 'c7dc529d8aae76b4e797e4e9e3ea7cd69669e6c3bb3f94d80f1974d1b9f69378'
url = 'https://www.virustotal.com/vtapi/v2/file/report'

# Parameters that are sent with the request including API Key and Resource ID. 
# Some services require additional params
params = {'apikey': apiKey,'resource':resource}


response = requests.get(url, params=params)
#results = response.json()
print("Pretty JSON:",json.dumps(response.json(), indent=2))

