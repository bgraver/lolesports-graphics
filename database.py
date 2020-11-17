import pymongo
import json


def load_keys():
    with open("database.keys") as f:
        key = json.load(f)
    return key

def connect_db(keys):
    return pymongo.MongoClient("mongodb+srv://{0}:{1}@{2}/{3}?retryWrites=true&w=majority".format(keys['username'], keys['password'], keys['address'], keys['databaseName']))

