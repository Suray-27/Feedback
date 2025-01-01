from pymongo import MongoClient # Required Library
import os
from io import BytesIO
#from bson.binary import Binary
import joblib
from dotenv import load_dotenv

load_dotenv()

# Initiate Database
client = MongoClient(os.getenv("MONGODB_PASSWORD")) # Credentials
db = client["Model_db"]
collection = db["models"]

"""def save_model_to_mongodb(model, model_name):
    # Serialize the model into memory
    buffer = BytesIO()
    joblib.dump(model, buffer)
    buffer.seek(0)  # Move to the beginning of the buffer
    
    # Create binary data
    model_binary = Binary(buffer.read()) 
    
    # Store the model in MongoDB
    collection.replace_one(
        {"name": model_name},
        {"name": model_name, "data": model_binary},
        upsert=True
    )

# Load models using joblib
scaler = joblib.load("Model/scale.pkl")
logistic_model = joblib.load("Model/logistic_model.pkl")
tfidf_vectorizer = joblib.load("Model/tfidf.pkl")

save_model_to_mongodb(scaler, "standard_scaler")
save_model_to_mongodb(logistic_model, "logistic_regression")
save_model_to_mongodb(tfidf_vectorizer, "tfidf_vectorizer")"""

def load_model_from_mongodb(model_name):
    # fetch the model from mongodb

    model_data = collection.find_one({"name": model_name})
    if not model_data:
        raise ValueError(f"Model {model_name} not found in MongoDB.")

    # Deserialize the binary data
    binary_data = model_data["data"]
    model = joblib.load(BytesIO(binary_data))
    return model

