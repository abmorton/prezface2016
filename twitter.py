import tweepy
import os


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# status = "Testing; tweeting from Python"
# api.update_status(status=status)


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	print tweet.text


user = api.get_user('HillaryClinton')

print user.screen_name
print user.followers_count

