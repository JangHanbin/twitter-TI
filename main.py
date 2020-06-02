import configparser
from dbconfig import Database
from twitter_api import Twitter
import logging
from time import sleep

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
    tweets = database.get_table('tweets')

    twitter_config = configparser.ConfigParser()
    twitter_config.read('api.ini')
    consumer_key = twitter_config['twitter']['api_key']
    consumer_secret = twitter_config['twitter']['api_secret_key']
    access_token_key = twitter_config['twitter']['access_token']
    access_token_secret = twitter_config['twitter']['access_token_secret']

    twitter = Twitter(consumer_key, consumer_secret, access_token_key, access_token_secret)

    logger = logging.getLogger('logger')
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[ %(levelname)s | %(filename)s: %(lineno)s] %(asctime)s > %(message)s')
        file_handler = logging.FileHandler('log.log')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)


    while True:
        for twitter_id in database.select(experts.columns.twitter_id):
            since_id = database.select(experts.columns.since_id, experts.columns.twitter_id == twitter_id)[0]
            if not since_id:
                since_id=0

            data = twitter.get_all_timeline(twitter_id, since_id=since_id)

            if not data:
                continue

            since_id = data[0][0] # to update since_id, set since_id to largest id_str
            database.update_since_id(experts, since_id, experts.columns.twitter_id==twitter_id)
            logger.info('Update since_id {0} to {1}'.format(since_id, twitter_id))

            for tweet in data:
                database.insert(tweets, tweet)
                logger.info('Success insert {0}'.format(tweet))

        logger.info('The cycle has been complete. retry after 600 secs..')
        sleep(600)




