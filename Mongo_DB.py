from pymongo import MongoClient
from urllib.parse import quote_plus
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


password = quote_plus(os.getenv("MONGODB_PASSWORD"))

try:
    client = MongoClient(f"mongodb+srv://capstone:{password}@capstone.sb2ut.mongodb.net/?retryWrites=true&w=majority&appName=capstone")
    print("Connected to MongoDB!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("Error:", e)



"""client = MongoClient("mongodb://localhost:27017/")
print("Databases on server:", client.list_database_names())
class MongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["customer_reviews"]
        self.collection = self.db["reviews"]

    def save_review_reply(self, user_review, reply, sentiment):
        self.collection.insert_one({"review": user_review, "reply": reply, "sentiment": sentiment})

    def get_reviews(self):
        reviews = self.collection.find({}, {"_id": 0})
        return pd.DataFrame(list(reviews))
    

get_reviews = MongoDB().get_reviews()

if __name__ == "__main__":
    reviews_df = get_reviews
    print(reviews_df)"""