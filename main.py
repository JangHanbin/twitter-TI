import configparser
from dbconfig import Database
from twitter_api import Twitter


if __name__=='__main__':

    db_config = configparser.ConfigParser()
    db_config.read('dbconfig.ini')
    host = db_config['DEFAULT']['HOST']
    db_id = db_config['DEFAULT']['ID']
    passwd = db_config['DEFAULT']['PASSWD']
    db_name = db_config['DEFAULT']['DATABASE']


    database = Database(db_id, passwd, host, db_name)

    keywords = database.get_table('keywords')
    experts = database.get_table('experts')


    twitter_config = configparser.ConfigParser()
    twitter_config.read('api.ini')
    consumer_key = twitter_config['twitter']['api_key']
    consumer_secret = twitter_config['twitter']['api_secret_key']
    access_token_key = twitter_config['twitter']['access_token']
    access_token_secret = twitter_config['twitter']['access_token_secret']

    twitter = Twitter(consumer_key, consumer_secret, access_token_key, access_token_secret)
    tweets = twitter.get_timeline('cyberwar')
    for tweet in tweets:
        print(tweet)



