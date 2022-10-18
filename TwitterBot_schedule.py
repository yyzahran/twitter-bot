import tweepy
import time
import schedule
import random
from crontab import CronTab

# logging in
consumer_key = "" # API KEY
consumer_secret = "" # API SECRET KEY
bearer_key = """""" # BEARER KEY
access_token = ""
access_token_secret = ""

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
