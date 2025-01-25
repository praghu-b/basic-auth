import logging
from pymongo import MongoClient

logger = logging.getLogger(__name__)

db = None

def connect_db():
    global db
    if db is None:
        try:
            client = MongoClient('mongodb+srv://prakashbalan555:prakashbalan555@ai-course.si9g6.mongodb.net/')
            db = client['social_media']
            print('DB Connected Successfully...')
        except Exception as e:
            print('Error occurred while trying to connect the db: %s', e)
            db = None
    return db

