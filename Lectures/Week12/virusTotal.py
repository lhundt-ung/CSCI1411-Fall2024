import requests
import json
# VirusTotal API Documentation - https://developers.virustotal.com/reference/overview

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
apiKey = '<API KEY>'

params = {'apikey': apiKey}
files = {'file': ('/home/kali/Downloads/ransomware.exe', open('/home/kali/Downloads/ransomware.exe', 'rb'))}

# Look at the requests method. This is different than GET
response = requests.post(url, files=files, params=params)

#Ugly JSON
print("UGLY JSON:",response.json())

#Print JSON a little prettier :)
print("Pretty JSON:",json.dumps(response.json(), indent=2))
#print("Resource ID:",response.json()["resource"])


