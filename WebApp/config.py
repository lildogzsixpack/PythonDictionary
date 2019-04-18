import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

flask_key = config.get('main', 'flask_key')
host = config.get('main', 'host')
port = config.get('main', 'port')
debug = config.get('main', 'debug')
