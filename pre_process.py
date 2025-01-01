from nltk.corpus import stopwords # Required Libraries
from textblob import TextBlob
import re
import emoji
import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# To clean text
def preprocess(text):
    sub_text = text.lower().strip()
    extracted_emojis = ''.join(char for char in text if char in emoji.EMOJI_DATA)
    sub_text = re.sub(r'[^\w\s]', '', sub_text)
    important_words = {'but', 'than','try uber'}
    sub_text = ' '.join([word for word in sub_text.split() if word not in stop_words or word in important_words])
    return sub_text+''+extracted_emojis


# Classify sentiments
def analyze_sentiment(text,competitors):

    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    negative_keywords = ['bad', 'terrible', 'poor', 'disappointing', 'hate', 'worst']
    company_keywords = ['Ola', 'driver', 'ride', 'app', 'cab', 'service']
    competitor_mentioned = any(comp in text.lower() for comp in competitors)

    if competitor_mentioned and ("expensive" in text.lower()
                                 or "extra charge" in text.lower()
                                 or 'hangs' in text.lower()
                                 or "cutomer support" in text.lower()):
        
        return "negative"
    
    if any(keyword in text.lower() for keyword in negative_keywords) or any(keyword in text.lower() for keyword in company_keywords):
        return "negative"
    

    if polarity > 0:
        return 'positive'
    if polarity < 0:
        return 'negative'
    else:
        return 'neutral'
    
    
