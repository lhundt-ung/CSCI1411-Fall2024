import requests
import json
from requests.auth import HTTPBasicAuth

# Wifi Hotspot Mac Addresses found on computer
wifiHotspot = ['00:30:65:03:e8:c6','00:0b:85:23:23:3e']

# API Authentication
key = ""
token = ""

apiAuth = (key,token)

#Example API query: https://api.wigle.net/api/v2/network/detail?netid=00%3A11%3A50%3A24%3A68%3A7F-H "accept: application/json"

#Function to lookup a Hotspot Mac Address
def lookupMac(mac):
    convertedMac = mac.replace(":","%3A")
    r = requests.get("https://api.wigle.net/api/v2/network/detail?netid=" + convertedMac, auth=apiAuth)
    wigleJSON = r.json()
    printLocation(wigleJSON)

def printLocation(j):
    print("+ SSID Name: ",j['results'][0]['ssid'])
    print("     -Latitude:",j['results'][0]['trilat'],"Longitude:",j['results'][0]['trilong'])
    print("     -State:",j['results'][0]['region'],"Country:",j['results'][0]['country'])


def main():
    for macAddress in wifiHotspot:
        lookupMac(macAddress)

if __name__ == "__main__":
    main()