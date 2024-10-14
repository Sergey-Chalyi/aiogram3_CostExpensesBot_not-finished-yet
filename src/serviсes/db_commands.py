# services/user_service.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from aiogram.types import Message
from datetime import datetime, timezone
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_client = AsyncIOMotorClient(mongo_uri)
db = mongo_client["users_info"]
collection = db["users"]

async def register_user(message: Message):
    if not await does_user_exist(message):
        await add_user_data(message)

async def does_user_exist(message: Message):
    return await collection.find_one({"user_id": message.from_user.id})

async def add_user_data(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    is_premium = message.from_user.is_premium if hasattr(message.from_user, 'is_premium') else False
    registration_date = datetime.now(timezone.utc)

    await collection.insert_one({
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "is_premium": is_premium,
        "registration_date": registration_date
    })
