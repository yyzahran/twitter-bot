import tweepy
import time
import schedule
import random

# logging in
consumer_key = "xCkC9VMdgmRtyLWpz1FGMgKH5" # API KEY
consumer_secret = "8RSVwnnG06zApTKQVyxOIJqMEmgXjUxiTidrq5h3aVdEyvihlZ" # API SECRET KEY
bearer_key = """AAAAAAAAAAAAAAAAAAAAALxGLgEAAAAAOk4nvPLf4%2F%2BwspCiaDGlKyF1YbA%3Dt33TdvGQfjMhmUZo3N7peBipBkJhfivduhWBEDbqP5r6dSC3Kb""" # BEARER KEY
access_token = "1348505272780607489-8GNvEZZVCkRQT76nNdk3Pn75UuYr6I"
access_token_secret = "XwEDZl0o45y8RKVxTqMD9TG3HLJ0X6Y8ubrTe1HZghlwN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# function to post a tweet everyday
def tweet_daily(tweet):
    api.update_status(tweet)


# open the lyrics file and generate a random line
with open('radioheadLyrics.txt', 'r') as lyrics_file:
    l = []
    for lines in lyrics_file.readlines():
        if not lines.strip():
            continue
        if lines.isalpha:
            l.append(lines.rstrip())
    daily_tweet = random.choice(l)


# schedule.every().day.at('08:00').do(tweet_daily)

tweet_daily(daily_tweet)

schedule.every(10).minutes.do(tweet_daily(daily_tweet))

# debugging
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.me()

# # tweet_daily('Tweet from VScode sssagain!')

# print(user.screen_name) # returns handle name