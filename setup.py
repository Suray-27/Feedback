import nltk
from nltk.corpus import stopwords
from pre_process import preprocess
from email_utils import email_coupon
from mongo_db import load_model_from_mongodb
from ai_response import generate_reply

# Use stopwords in your app
stop_words = stopwords.words('english')