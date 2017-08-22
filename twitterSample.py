
'''
import twitter

CONSUMER_KEY = 'neB4RoDJ1MzigFlHlCPAe3l13'
CONSUMER_SECRET = 'TVGlmXUjhsLTqnMPBWAbrkRRcBdPdHER5rM7DTaa3xdjInHmLG'
OAUTH_TOKEN = '1559425693-1l6l28ql60COAdZuQBYDWqRgrbry6kGhCo57QUu'
OAUTH_TOKEN_SECRET = 'gMTrtjIVyXSrNDS4q76dopIYPJbwpYFGgW2bDA7eJuKLI'

api = twitter.Api(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

print(api)
'''


import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'neB4RoDJ1MzigFlHlCPAe3l13'
consumer_secret = 'TVGlmXUjhsLTqnMPBWAbrkRRcBdPdHER5rM7DTaa3xdjInHmLG'
access_token = '1559425693-1l6l28ql60COAdZuQBYDWqRgrbry6kGhCo57QUu'
access_secret = 'gMTrtjIVyXSrNDS4q76dopIYPJbwpYFGgW2bDA7eJuKLI'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# print 10 tweets from timeline
'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
'''

# Get the User object for twitter...
'''
user = api.get_user('twitter')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
 '''


lat = 40.7128
lon = 74.0059
trends = api.trends_closest(lat, lon)
for trend in trends:
	print(trend)

