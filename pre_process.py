from nltk.corpus import stopwords
from textblob import TextBlob
import emoji
import re


stop_words = set(stopwords.words('english'))

def preprocess(text):
    sub_text = text.lower().strip()
    extracted_emojis = ''.join(char for char in text if char in emoji.EMOJI_DATA)
    sub_text = re.sub(r'[^\w\s]', '', sub_text)
    important_words = {'but', 'than','try uber'}
    sub_text = ' '.join([word for word in sub_text.split() if word not in stop_words or word in important_words])
    return sub_text+''+extracted_emojis


def analyze_sentiment(text,competitors):

    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    competitor_mentioned = any(comp in text.lower() for comp in competitors)

    if competitor_mentioned and ("expensive" in text.lower() or "better" in text.lower()
                                 or "extra charge" in text.lower()
                                 or 'hangs' in text.lower()):
        
        return "negative"

    if polarity > 0:
        return 'positive'
    if polarity < 0:
        return 'negative'
    else:
        return 'neutral'
    