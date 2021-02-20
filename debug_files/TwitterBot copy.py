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


# open the lyrics file and generate a random line
def extract_lyric_line():
    with open('radioheadLyrics.txt', 'r') as lyrics_file:
        l = []
        for lines in lyrics_file.readlines():
            if not lines.strip():
                continue
            if lines.isalpha:
                l.append(lines.rstrip())
        # return daily_tweet = random.choice(l)
        return random.choice(l)
        # print(random.choice(l)) # TODO delete this line

# extract_lyric_line()
# function to post a tweet everyday
def tweet_daily():
    try:
        api.update_status(extract_lyric_line())
    except tweepy.TweepError as error:
        if error.api_code == 187:
        # Do something special
            print('Duplicate tweet!', extract_lyric_line())
            api.update_status(extract_lyric_line())
        else:
            raise error
    # api.update_status(daily_tweet)


# # timing
schedule.every(1).minutes.do(tweet_daily)

while True:
    schedule.run_pending()
    time.sleep(1)





# debugging
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()

# tweet_daily('Tweet from VScode sssagain!')

print(user.screen_name) # returns handle name