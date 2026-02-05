from pymongo import MongoClient
import os 
import json


MONGO_HOST = os.getenv("MONGO_HOST","localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT","27017"))
MONGO_DATABASE = os.getenv("MONGO_DATABASE","test_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION","test_collection")


URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"


class MongoManger():
    def __init__(self):
        self.client = MongoClient(URI)
        self.db = self.client[MONGO_DATABASE]
        self.collection = self.db[MONGO_COLLECTION]

        
    def init_data(self):
        with open("./employee_data_advanced.json",'r') as file:
            data = file.read()
            res = json.loads(data)
            self.collection.drop()
            self.collection.insert_many(res)



manager = MongoManger()
