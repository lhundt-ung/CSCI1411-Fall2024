import requests
import json
import sendTweet
import chatgptapi
from datetime import *


covidAPIURL = "https://api.covidtracking.com/v1/states/ga/daily.json"

# Get Georgia daily Confirmed cases in time span
# Used daterange code from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Part 1 - Write a script that prints out the COVID cases confirmed for Georgia between two dates?
# This API Service stopped collecting data on 3/1/2021
def getGACovidCases():  
    start_date = date(2020, 8, 1)
    end_date = date(2020, 8, 6)
    message = "Georgia daily COVID Cases between " + str(start_date) + " and " + str(end_date) + "\n"

    #CODE HERE
    for single_date in daterange(start_date,end_date):
        single_date = single_date.strftime("%Y%m%d")
        r = requests.get(covidAPIURL)
        georgia = r.json()
        #print(single_date)
        #print(georgia[0])

        for day in georgia:
            #print(str(day["date"]), single_date)

            if str(day["date"]) == str(single_date):
                dailyTotal = str(single_date) + " - " + str(day["positiveIncrease"])
                message += dailyTotal + "\n"

    return message


def main():
    tweet = getGACovidCases()
    print(tweet)

    #PART 2: How could we call our tweet function from another script?
    sendTweet.post(tweet)

    #PART 3: Use ChatGPT to gather COVID cases, then tweet the response :)
    answer = chatgptapi.askChatGPT("Tell me the daily COVID Cases for Georgia between 8/1/2020 to 8/5/2020 from this source https://api.covidtracking.com/v1/states/ga/daily.json")
    
    print(answer)
    gptCaseAnswer = "Last 5 days of Georgia COVID Cases \n"
    for line in answer.split("\n"):
        if "- " in line:
            print(line)
            gptCaseAnswer += line + "\n"
    print(gptCaseAnswer)
    sendTweet.post(gptCaseAnswer)

if __name__ == "__main__":
    main()