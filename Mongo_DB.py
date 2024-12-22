from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_PASSWORD"))
db = client["feedback_db"]
collection = db["reviews"]


class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_PASSWORD"))
        self.db = self.client["customer_reviews"]
        self.collection = self.db["reviews"]

    def save_review_reply(self, user_review, reply, sentiment):
        self.collection.insert_one({"review": user_review, "reply": reply, "sentiment": sentiment})

    def get_reviews(self):
        reviews = self.collection.find({}, {"_id": 0})
        return pd.DataFrame(list(reviews))
    

get_reviews = MongoDB().get_reviews()

