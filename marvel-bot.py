from TwitterAPI import TwitterAPI
import os


TWEET_TEXT = "I feel most alive when I am dancing"
IMAGE_PATH = './dancing_kang.jpg'

api = TwitterAPI(os.environ['TWITTER_CONSUMER_KEY'],
                 os.environ['TWITTER_CONSUMER_SECRET'],
                 os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                 os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

file = open(IMAGE_PATH, 'rb')
data = file.read()
r = api.request('statuses/update_with_media',
                    {'status': TWEET_TEXT},
                    {'media[]': data})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
