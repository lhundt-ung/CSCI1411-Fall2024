import shodan
import sys
import requests
import json

#Shodan API - https://developer.shodan.io/api
#Shodan Python Library - https://shodan.readthedocs.io/en/latest/ 

#Examples of Use Shodan's Python library module vs requests module

#Setup API Access
SHODAN_API_KEY = "<API KEY>"


# API access via Requests method
#searchTerm = input("Enter the search query: ")
#url = "https://api.shodan.io/shodan/host/search?key="+SHODAN_API_KEY+"&query="+searchTerm
#r = requests.get(url)
#Output json with identions (Way cleaner to read)
#print(json.dumps(r.json(), indent=2))


# Second method, using prebuilt Python library called Shodan
#api = shodan.Shodan(SHODAN_API_KEY)
#results = api.search('ung.edu')
#print(json.dumps(results['matches'],indent=2))


# Build a function to use Shodan Search Service. Reurns all results and prints out originating Country


def searchShodan(apiKey,query):
        api = shodan.Shodan(SHODAN_API_KEY)
        findings = []
        results = api.search(query)
        for result in results['matches']:
                print("Location: ", result['location']['country_name'])
                finding = {"IP":result["ip_str"], "Location":result['location']['country_name']}
                findings.append(finding)

        for finding in findings:
                print("=============")
                for key,value in finding.items():
                        print("+",key,":",value)
        
        print(type(results))
        print("Total Results found: {}".format(results['total']))


# Search Shodan Function
searchShodan(SHODAN_API_KEY,'WebCam')

