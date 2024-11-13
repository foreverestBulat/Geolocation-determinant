from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB, MONGODB_URL

class MongoDBClient:
    def __init__(self, config = None):
        self.config = {
            'database_url': MONGODB_URL,
            'db_name': MONGODB['NAME']
        }
        self.client = None

    async def create_connection(self):
        if self.client is None:
            self.client = AsyncIOMotorClient(
                self.config['database_url']
            )
            db_list = await self.client.list_database_names()
            if self.config['db_name'] not in db_list:
                self.client[self.config['db_name']]
        return self.client

    def get_collection(self, collection_name):
        client = self.create_connection()
        db = client[collection_name]
        return db
    

async def get_db():
    factory = MongoDBClient()
    client = await factory.create_connection()
    db = client.get_database('save_ips')
    collection = db.get_collection('ips')
    return collection