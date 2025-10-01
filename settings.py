import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Database
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "neatseed")
    
    # OLA Maps
    OLAMAPS_API_KEY = os.getenv("OLAMAPS_API_KEY")
    
    # Firebase
    FIREBASE_SERVICE_ACCOUNT_PATH = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
    
    # Server
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Proximity settings
    NOTIFICATION_RADIUS_METERS = 100
    LOCATION_UPDATE_INTERVAL = 5  # seconds

settings = Settings()
