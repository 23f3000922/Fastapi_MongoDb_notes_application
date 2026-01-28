from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Jashan:jashan@fastapi.xlbtcxx.mongodb.net/notes"

conn = MongoClient(MONGO_URI)
