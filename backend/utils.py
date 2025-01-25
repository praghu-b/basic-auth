import os
from pymongo import MongoClient

def connect_db():
    try:
        client = MongoClient(os.getenv('MONGOURI'))
        db = client['social_media']
        print('DB Connected Successfully...')
    except Exception as e:
        print('Error occurred while trying to connect the db: %s', e)
        db = None
