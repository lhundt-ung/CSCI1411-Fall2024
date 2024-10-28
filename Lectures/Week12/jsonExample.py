import json

# some JSON:
jsonFile = '''{ 
            "name":"John", 
            "age":30, 
            "city":"New York",
            "cars": {
                "car1":"Ford",
                "car2":"BMW",
                "car3":"Fiat"
                }
            }'''

jsonDictionary = json.loads(jsonFile)

for car in jsonDictionary['cars']:
    print(jsonDictionary['cars'][car])