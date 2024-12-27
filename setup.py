import nltk
from nltk.corpus import stopwords
import pre_process
import email_utils
import mongo_db
import ai_response

# Use stopwords in your app
stop_words = stopwords.words('english')