#twitter API example
import requests
import json
import re

#Token for auth to twitter
bearer_token = ""

#Can we extend this to take an argument that generalizes the twitter account?
#urlexample: "https://api.twitter.com/2/tweets/search/recent?query=from:elonmusk&tweet.fields=author_id"

def create_url(twitter_handle):
    url = "https://api.twitter.com/2/tweets/search/recent?query=from:" + twitter_handle + "&tweet.fields=author_id"
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers
    
def connect_to_endpoint(url, headers):
    response = requests.request("GET",url, headers=headers)
    print(response.status_code)
    if (response.status_code != 200):
        raise Exception(response.status_code, response.text)
    return response.json()

def displayTweets(json):
    for tweet in json['data']:
        print(tweet['text'])
        print("--------------------")
    return

# Parse out only Hashtags
def displayHashtags(json):
    for tweet in json['data']:
        regex = r"\B#\w*[a-zA-Z]+\w*"
        #regex = r"*\B#*"
        hashtags = re.findall(regex,tweet['text'])
        print(hashtags)
        print("-----------------------")
    return
    
def main():
    #Example API URL:
    #url = "https://api.twitter.com/2/tweets/search/recent?query=from:elonmusk&tweet.fields=author_id"

    #Extend Create URL method to search for user
    url = create_url("uofnorthgeorgia")

    print(url)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))

    #Write a function that only displays tweets
    #displayTweets(json_response)
    
    #Example of extracting Hashtags
    displayHashtags(json_response)


if __name__ == "__main__":
    main()