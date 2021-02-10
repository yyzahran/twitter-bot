import tweepy
import time
import schedule
import random
from crontab import CronTab

# logging in
consumer_key = "xCkC9VMdgmRtyLWpz1FGMgKH5" # API KEY
consumer_secret = "8RSVwnnG06zApTKQVyxOIJqMEmgXjUxiTidrq5h3aVdEyvihlZ" # API SECRET KEY
bearer_key = """AAAAAAAAAAAAAAAAAAAAALxGLgEAAAAAOk4nvPLf4%2F%2BwspCiaDGlKyF1YbA%3Dt33TdvGQfjMhmUZo3N7peBipBkJhfivduhWBEDbqP5r6dSC3Kb""" # BEARER KEY
access_token = "1348505272780607489-8GNvEZZVCkRQT76nNdk3Pn75UuYr6I"
access_token_secret = "XwEDZl0o45y8RKVxTqMD9TG3HLJ0X6Y8ubrTe1HZghlwN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# open the lyrics file and generate a random line
def extract_lyric_line():
    with open('radioheadLyrics.txt', 'r') as lyrics_file:
        l = []
        for lines in lyrics_file.readlines():
            if not lines.strip():
                continue
            if lines.isalpha:
                l.append(lines.rstrip())
        return random.choice(l)


# function to post a tweet everyday
def tweet_daily():
    try:
        api.update_status(extract_lyric_line())
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('Duplicate tweet!', extract_lyric_line())
        else:
            raise error


# timing
schedule.every(1).day.at('11:00').do(tweet_daily)

while True:
    schedule.run_pending()
    time.sleep(1)
