from decouple import config
import json

import requests
from requests_oauthlib import OAuth1

from predict import get_prediction

def get_tweets(*args, count=10):
    """
    Get a number of tweets
    """
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    tweets = []

    for search_terms in args:
        params = {'q': search_terms, 'lang': 'en', 'count': count}
        response = requests.get(url, auth=auth, params=params)
        tweets += response.json()['statuses']
    
    return tweets

with open(config('TWITTER_CREDENTIALS'), 'r') as f:
    secrets = json.load(f)

auth = OAuth1(
    secrets['api_key'],
    secrets['api_secret_key'],
    secrets['access_token'],
    secrets['access_token_secret']
)

if __name__ == "__main__":
    # prompt a user for search terms 
    search_terms = input("Enter search terms separated by commas: ")
    search_terms = search_terms.split(',')
    tweets = get_tweets(search_terms)

    # save the tweets to a local file for analysis
    with open('tweets.json', 'w') as f:
        json.dump(tweets, f, indent=4, separators=(",", ":"))

    # output sentiment predictions of tweets
    for tweet in tweets:
        prediction_response = get_prediction(tweet['text'])
        if prediction_response.status_code == 200:
            print('TWEET:\n  {} \n'.format(tweet['text']))
            print(prediction_response.text, '\n')
        else:
            print('An error occured')

