import tweepy
# import twitter
import os
from app import db
from models import Candidate

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


candidates = Candidate.query.all()

for c in candidates:

	user = api.get_user(c.twitter_name)

	tweet_data = repr(api.user_timeline(screen_name=user.screen_name, count=400, include_rts=False))
	# tweet_data = repr(tweet_data)
	tweet_data_list = tweet_data.split('Status(')
	tweet_list_to_write = []

		# Nice visual representation in the shell.
	print "Database ID: {}".format(c.id)
	print "Twitter ID: {}".format(user.id)
	print "Twitter name: {}".format(user.screen_name)
	print "Number of followers: {}".format(user.followers_count)
	print ''

	for tweet_data in tweet_data_list:
		tweet_text_to_end = tweet_data.partition('text=u')[2]
		tweet_text = tweet_text_to_end.partition(', is_quote_status=')[0]
		tweet_list_to_write.append(tweet_text)
		print tweet_text
		print ''

	print '- - -'*10
	print ''

# Writing to /static/txt/ into .txt files, which will be used to create wordclouds.
	tweetfile = open("static/txt/"+str(c.id)+".txt", "wb")
	for item in tweet_list_to_write:
		tweetfile.write("%s\n" % item)
	tweetfile.close()



