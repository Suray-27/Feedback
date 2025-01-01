from pymongo import MongoClient # Required Library
import os
from io import BytesIO
import joblib
from dotenv import load_dotenv

load_dotenv()

# Initiate Database
client = MongoClient(os.getenv("MONGODB_PASSWORD")) # Credentials
db = client["Model_db"]
collection = db["models"]


def load_model_from_mongodb(model_name):
    # fetch the model from mongodb

    model_data = collection.find_one({"name": model_name})
    if not model_data:
        raise ValueError(f"Model {model_name} not found in MongoDB.")

    # Deserialize the binary data
    binary_data = model_data["data"]
    model = joblib.load(BytesIO(binary_data))
    return model

