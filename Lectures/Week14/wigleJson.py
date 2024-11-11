import json

#JSON Returned from Wigle
wigleJSON = {'success': True, 'cdma': False, 'gsm': False, 'lte': False, 'wcdma': False, 
'wifi': False, 'addresses': [], 'results': 
[{'trilat': 28.04605293, 'trilong': -82.60256195, 'ssid': 'LAX Airport', 
'qos': 2, 'transid': '20020728-00000', 'firsttime': 
'2002-07-27T14:31:23.000Z', 'lasttime': '2006-03-29T18:21:39.000Z', 
'lastupdt': '2017-07-27T03:39:55.000Z', 'netid': '00:30:65:03:e8:c6', 
'name': None, 'type': 'BSS', 
'comment': 'Appended by moxiao1995071310 on 2017-07-26 20:36:20:\n\n123\n\nAppended by moxiao1995071310 on 2017-07-26 20:39:50:\n\n123\n\nAppended by moxiao1995071310 on 2017-07-26 20:39:55:\n\n123',
 'wep': 'Y', 'bcninterval': 100, 'freenet': '?', 'dhcp': '?',
  'paynet': '?', 'userfound': None, 'channel': 1, 'locationData': [],
   'encryption': 'wep', 'country': 'US', 'region': 'FL', 'city': None,
    'housenumber': None, 'road': 'West Linebaugh Avenue', 'postalcode': '33626'}]}

print(json.dumps(wigleJSON,indent=2))
print("+ SSID Name: ",wigleJSON['results'][0]['ssid'])
print("     -Latitude:",wigleJSON['results'][0]['trilat'],"Longitude:",wigleJSON['results'][0]['trilong'])
print("     -State:",wigleJSON['results'][0]['region'],"Country:",wigleJSON['results'][0]['country'])