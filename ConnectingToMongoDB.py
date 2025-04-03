
import pymongo
from pymongo import MongoClient

# Replace with your actual VM's public IP
MONGO_URI = "mongodb://132.220.212.41:27017/"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database
db = client["myNewDatabase"]

# Select collection
collection = db["myCollection"]

# Insert a document
data = {"name": "Alice", "age": 25, "job": "Data Scientist"}
collection.insert_one(data)

# Fetch and print all documents
for doc in collection.find():
    print(doc)
