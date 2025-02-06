from fastapi import Depends
from models.user import User
from db.connection import MongoDB, get_db
from utils.serializers import individual_serial, individual_serials
from bson import ObjectId


class UserService:
    def __init__(self, db: MongoDB):
        self.collection = db.get_collection("users")

    async def create_user(self, user: User):
        user_data = user.model_dump()
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)
    
    async def get_all_users(self):
        return individual_serials(await self.collection.find().to_list(100))
    
    async def get_user_by_id(self, id: str):
        return individual_serial(await self.collection.find_one({"_id": ObjectId(id)}))

    async def get_user_by_email(self, email: str):
        return individual_serial(await self.collection.find_one({"email": email}))


def get_service(db: MongoDB = Depends(get_db)) -> UserService:
    return UserService(db)