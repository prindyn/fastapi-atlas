import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("MONGO_DB")]
    
    def get_collection(self, collection_name: str):
        return self.db[collection_name]

def get_db() -> MongoDB:
    return MongoDB()