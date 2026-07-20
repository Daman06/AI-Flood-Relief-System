

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

print("URI:", MONGO_URI)

client = MongoClient(MONGO_URI)

db = client["flood_relief"]

print("Database:", db.name)
print("Collections:", db.list_collection_names())

volunteers_collection = db["volunteers"]
rescue_requests_collection = db["rescue_requests"]