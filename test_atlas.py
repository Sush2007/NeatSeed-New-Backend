import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

async def test_mongodb_atlas():
    """Test MongoDB Atlas connection with Cluster0"""
    try:
        print("🚀 Starting MongoDB Atlas Connection Test...")
        print("=" * 50)
        
        # Get connection string from .env
        connection_string = os.getenv("MONGODB_URL")
        database_name = os.getenv("DATABASE_NAME", "neatseed")
        
        if not connection_string:
            print("❌ MONGODB_URL not found in .env file")
            print("Make sure your .env file has:")
            print("MONGODB_URL=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority")
            return
        
        print(f"🔍 Testing connection to MongoDB Atlas...")
        print(f"📋 Database name: {database_name}")
        print(f"🔗 Connection string: {connection_string[:60]}...")
        print("")
        
        # Connect to MongoDB Atlas Cluster0
        client = AsyncIOMotorClient(
            connection_string,
            serverSelectionTimeoutMS=5000
        )
        
        # Test connection with ping
        print("⏳ Pinging MongoDB Atlas...")
        await client.admin.command('ping')
        print("✅ Successfully connected to MongoDB Atlas Cluster0!")
        print("")
        
        # Get server info
        server_info = await client.server_info()
        print(f"📊 MongoDB Version: {server_info['version']}")
        print("")
        
        # Access the neatseed database
        db = client[database_name]
        collection = db["test_connection"]
        
        # Insert test document
        print("📝 Inserting test document...")
        test_doc = {
            "app": "NeatSeed",
            "message": "Hello from NeatSeed Backend!",
            "cluster": "Cluster0", 
            "database": database_name,
            "timestamp": datetime.now().isoformat(),
            "test_id": "connection_test_001"
        }
        
        result = await collection.insert_one(test_doc)
        print(f"✅ Inserted document with ID: {result.inserted_id}")
        
        # Read test document back
        print("📖 Reading document back...")
        found_doc = await collection.find_one({"_id": result.inserted_id})
        if found_doc:
            print(f"✅ Retrieved: {found_doc['message']}")
            print(f"✅ Database: {found_doc['database']}")
            print(f"✅ Cluster: {found_doc['cluster']}")
        
        # List all databases in the cluster
        print("\n🗂️  Available databases in Cluster0:")
        db_list = await client.list_database_names()
        for db_name in db_list:
            print(f"   - {db_name}")
        
        # Clean up test document
        print("\n🧹 Cleaning up test document...")
        await collection.delete_one({"_id": result.inserted_id})
        print("✅ Test document deleted")
        
        # Close connection
        client.close()
        print("\n🎉 MongoDB Atlas connection test completed successfully!")
        print("=" * 50)
        print("✅ Your backend is ready to use MongoDB Atlas Cluster0!")
        
    except Exception as e:
        print(f"\n❌ Connection test failed!")
        print(f"Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check your .env file has the correct MONGODB_URL")
        print("2. Make sure your MongoDB Atlas user password is correct")
        print("3. Verify IP whitelist includes your current IP (0.0.0.0/0 for testing)")
        print("4. Ensure your cluster is running (not paused)")

if __name__ == "__main__":
    print("🌱 NeatSeed MongoDB Atlas Connection Test")
    print("==========================================")
    
    # Run basic connection test
    asyncio.run(test_mongodb_atlas())
    
    print("\n🚀 Ready to start your NeatSeed backend!")
