import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['API_KEY']
api_key_secret = config['twitter']['API_KEY_SECRET']

access_token = config['twitter']['ACCESS_TOKEN']
access_token_secret = config['twitter']['ACCESS_TOKEN_SECRET']

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# create api object
api = tweepy.API(auth)

# get tweets by gelocation in lebanon
tweets = api.search_tweets(q="*", geocode="33.888629,35.495479,70km", count=50000)

# create dataframe
df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# write the list of tweets to a csv file 
df.to_csv('tweets.csv', index=False)

