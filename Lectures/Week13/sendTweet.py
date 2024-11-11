#Send Tweet
import requests
import json
# Use of tweepy module (Twitter API Wrapper) to post a tweet!
# pip3 install tweepy
import tweepy

CONSUMER_KEY =""
CONSUMER_SECRET = ""  
ACCESS_KEY = ""    
ACCESS_SECRET = ""


def post(message):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    twitter = tweepy.API(auth)
    twitter.update_status(message)

def getTrends():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    twitter = tweepy.API(auth)

    # List Countries
    print(json.dumps(twitter.available_trends(), indent=4))
    
    # Countries woeid (Where On Earth IDentifier)
    us_woeid = "23424977"
    #poland_woeid = "23424923"
    #russia_woeid = "23424936"

    # Example of get_place_trends(woeid number)
    #print(json.dumps(twitter.get_place_trends(us_woeid), indent=4))

    #Process JSON
    output = twitter.get_place_trends(us_woeid)
    print("********************")
    for result in output[0]["trends"]:
        print(" +",result["name"], "- Tweet Volume:",result["tweet_volume"] )
    return


def main():
    #POST TWEET Example
    #post("Hello Class Spring 2023!")

    #Get Trends
    getTrends()

if __name__ == "__main__":
    main()