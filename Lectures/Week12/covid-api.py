import requests
from datetime import *

state = "ga"
covidAPIURL = "https://api.covidtracking.com/v1/states/" + state + "/daily.json"
today = datetime.today().strftime('%Y-%m-%d')

r = requests.get(covidAPIURL)
gaCOVIDStats = r.json()
#print(gaCOVIDStats)


# Get Georgia daily Confirmed cases in time span
# Used daterange code from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 8, 1)
end_date = date(2020, 8, 5)
for single_date in daterange(start_date, end_date):
    single_date = single_date.strftime("%Y%m%d")
    r = requests.get(covidAPIURL)
    georgia = r.json()
    #print(single_date)

    for day in georgia:
        #print(str(day["date"]), single_date)    
        if str(day["date"]) == str(single_date):
            print(single_date," - Confirmed Cases:",day["positiveIncrease"])
