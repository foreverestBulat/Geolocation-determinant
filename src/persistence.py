from typing import Any
from fastapi import Depends, FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBClient:
    def __init__(self, config = None):
        self.config = {
            'database_url': 'mongodb://localhost:27017',
            'db_name': 'save_ip'
        }
        self.client = None

    def create_connection(self):
        if self.client is None:
            self.client = AsyncIOMotorClient(
                self.config['database_url']
            )

        return self.client

    def get_collection(self, collection_name):
        client = self.create_connection()
        db = client[collection_name]
        return db
    

def get_db():
    factory = MongoDBClient()
    # collection = factory.get_collection('ips')
    client = factory.create_connection()
    db = client.get_database('save_ips')
    collection = db.get_collection('ips')
    print(type(collection))
    return collection
    # return collectio