import requests
import configparser
from dbconfig import Database

if __name__=='__main__':

    config = configparser.ConfigParser()
    config.read('dbconfig.ini')
    host = config['DEFAULT']['HOST']
    db_id = config['DEFAULT']['ID']
    passwd = config['DEFAULT']['PASSWD']
    db_name = config['DEFAULT']['DATABASE']


    database = Database(db_id, passwd, host, db_name)

    keywords = database.get_table('keywords')
    users = database.get_table('users')



