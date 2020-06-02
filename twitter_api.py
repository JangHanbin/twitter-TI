import twitter as tw
import requests
from datetime import datetime


def parse_hashtag(hashtag):

    result = list()

    for hash in hashtag:
        result.append([hash.get('text')])

    return result

def get_full_text(tweet):
    if tweet.get('retweeted_status'):
        return tweet.get('retweeted_status').get('full_text')
    else:
        return tweet['full_text'] if tweet.get('full_text') else tweet['text']

class Twitter():
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tw.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret,
                          tweet_mode='extended')


    def get_timeline(self, user_id):
        tweets = self.api.GetUserTimeline(screen_name=user_id, max_id=1262748142778249220, count=20)
        return tweets

    def get_since_id(self, user_id):
        return

    def get_all_timeline(self,user_id, since_id = 0):
        result = list()
        while True:
            tweets = self.api.GetUserTimeline(screen_name=user_id, count=200, since_id= since_id, exclude_replies=True)
            if not tweets:
                return result

            for tweet in tweets:
                tweet = tweet.AsDict()

                id_str = int(tweet.get('id_str'))
                id = tweet.get('id')
                screen_name = user_id
                created_at = datetime.strptime(tweet.get('created_at'), '%a %b %d %H:%M:%S %z %Y')
                text = get_full_text(tweet)
                source = tweet.get('source')
                truncated = tweet.get('truncated')
                in_reply_to_status_id = tweet.get('in_reply_to_status_id')
                in_reply_to_user_id = tweet.get('in_reply_to_user_id')
                in_reply_to_screen_name = tweet.get('in_reply_to_screen_name')
                quoted_status_id = tweet.get('quoted_status_id')
                is_quote_status = tweet.get('is_quote_status')
                quote_count = tweet.get('quote_count')
                reply_count = tweet.get('reply_count')
                retweet_count = tweet.get('retweet_count')
                favorite_count = tweet.get('favorite_count')
                favorited = tweet.get('favorited')
                retweeted = tweet.get('retweeted')
                lang = tweet.get('lang')
                retweeted_status_id = int(tweet['retweeted_status'].get('id_str')) if tweet.get('retweeted_status') else None  # if
                search_stamp = datetime.now()


                result.append([id_str, id, screen_name, created_at, text, source, truncated, in_reply_to_status_id, in_reply_to_user_id, in_reply_to_screen_name, quoted_status_id, is_quote_status,
                 quote_count, reply_count, retweet_count, favorite_count, favorited, retweeted, lang, retweeted_status_id, search_stamp])

            since_id = tweets[0].AsDict()['id']



