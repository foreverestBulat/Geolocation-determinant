from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB, MONGODB_URL

class MongoDBClient:
    def __init__(self, config = None):
        self.config = {
            'database_url': MONGODB_URL,
            'db_name': MONGODB['NAME']
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
    client = factory.create_connection()
    db = client.get_database('save_ips')
    collection = db.get_collection('ips')
    return collection