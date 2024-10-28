import requests
import json

apiURL = 'https://api.covidtracking.com/v1/states/ga/daily.json'

#Part 1 - Write a script that prints out the current COVID cases confirmed for Georgia?
# This API Service stopped collecting data on 3/1/2021

r = requests.get(apiURL)
print(r.json())
#print(json.dumps(r.json(), indent=2))

georgia=r.json()

for x in range(0,10):
    print(georgia[x]['date'],":",georgia[x]['positive'])



