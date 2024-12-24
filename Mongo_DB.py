from pymongo import MongoClient
import os
from io import BytesIO
import joblib
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_PASSWORD"))
db = client["Model_db"]
collection = db["models"]

def load_model_from_mongodb(model_name):
    # fetch the model from mongodb

    model_data = collection.find_one({"name": model_name})
    if not model_data:
        raise ValueError(f"Model {model_name} not found in MongoDB.")

    # Deserialize the binary data
    model = joblib.load(BytesIO(model_data["data"]))
    return model
