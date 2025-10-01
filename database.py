

from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from app.config.settings import settings


class Database:
    def __init__(self):
        self.client: Optional[AsyncIOMotorClient] = None

database = Database()

async def get_database():
    if database.client is None:
        raise RuntimeError("Database client is not connected.")
    return database.client[settings.DATABASE_NAME]

async def connect_to_mongo():
    """Create database connection"""
    database.client = AsyncIOMotorClient(settings.MONGODB_URL)
    print("Connected to MongoDB")

async def close_mongo_connection():
    """Close database connection"""
    if database.client:
        database.client.close()
        print("Disconnected from MongoDB")
