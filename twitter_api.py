import twitter as tw
import requests


class Twitter():
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tw.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


    def get_timeline(self, user_id):
        tweets = self.api.GetUserTimeline(screen_name=user_id, max_id=1262748142778249220, count=20)
        return tweets


