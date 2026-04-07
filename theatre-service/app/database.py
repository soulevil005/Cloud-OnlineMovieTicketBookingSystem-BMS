from pymongo import MongoClient

MONGO_URL = "mongodb+srv://admin:admin123@clusterbms.sg0sjud.mongodb.net/bookmyshow?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)
db = client["bookmyshow"]

theatre_collection = db["theatres"]