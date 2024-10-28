import json
#LargeDictionaryExample = 'https://api.covidtracking.com/v1/states/ga/daily.json'
dictionary = {"name":"John", "age":30, "city":"New York","cars": {"car1":"Ford","car2":"BMW", "car3":"Fiat"}}

# Normal Dictionary Print
print(dictionary)

# Use json.dumps() to add indentation. You can use on any dictionary object
#print(json.dumps(dictionary,indent=2))
print(json.dumps(dictionary,indent=2,sort_keys=True))