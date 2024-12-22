from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_PASSWORD"))
db = client["feedback_db"]
collection = db["reviews"]

cursor = collection.find()

for record in cursor:
    print(record)

