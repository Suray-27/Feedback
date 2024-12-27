import os
from datetime import datetime
from scipy.sparse import hstack
from mongo_db import load_model_from_mongodb
from pre_process import preprocess
import re
import streamlit as st
from pymongo import MongoClient
from ai_response import generate_reply
from email_utils import email_coupon


# Set up the Streamlit app configuration
st.set_page_config(page_title="Customer Response Generator")

# Initialize session state variables for navigation and user login
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None

# Initialize MongoDB client and database connection
@st.cache_resource
def get_mongo_client():
    return MongoClient(os.getenv("MONGODB_PASSWORD"))

def get_mongo_collection():
    client = get_mongo_client()
    db = client["feedback_db"]
    return db["reviews"]


@st.cache_resource
def get_models():
    # Retrieve models from MongoDB
    scaler = load_model_from_mongodb("standard_scaler")
    tfidf = load_model_from_mongodb("tfidf_vectorizer")
    logistic_model = load_model_from_mongodb("logistic_regression")
    return scaler, tfidf, logistic_model

# Load models and MongoDB collection
collection = get_mongo_collection()
scaler, tfidf, logistic_model = get_models()



# Helper function to change pages
def change_page(new_page):
    st.session_state.page = new_page

if st.session_state.page == "Home":
    st.title("Customer reply generator")
    st.header("User Login")

    with st.form("login_form"):
        user_email = st.text_input("Enter Your Email:", placeholder="e.g., user@gmail.com")
        login_button = st.form_submit_button("Login")

        #Login button
        if login_button:
            if re.match(r"^[\w\.-]+@gmail\.com$", user_email):
                st.session_state.logged_in = True
                st.session_state.user_email = user_email
                st.success("User logged in successfully.")
                change_page("User Reviews")
            else:
                st.error("Please enter a valid email address.")


# User Reviews Page: Review submission and sentiment analysis
elif st.session_state.page == "User Reviews":
    st.title("Customer Reviews")

    # Ensure the user is logged in before showing review options
    if st.session_state.logged_in:

        # Input field for user review
        user_review = st.text_area("Enter Your Review:",placeholder="Write your review here...")

        # Radio buttons for rating selection
        rat = st.radio("Your Rating", [1, 2, 3, 4, 5])
        

        # Button to generate AI-based reply
        if st.button("Submitt Response"):
            # Ensure the review is not empty
            if not user_review.strip():
                st.error("Please enter a review.")
                st.stop()
            else:
                # Preprocess and vectorize the review
                cleaned_review = preprocess(user_review)
                vectorized_review = tfidf.transform([cleaned_review])
                rating = scaler.transform([[rat]])
                combine = hstack([vectorized_review,rating])

                # Predict sentiment using the trained model
                sentiment = logistic_model.predict(combine)
                sentiment = str(sentiment[0])

                # Generate a response based on sentiment

                reply = generate_reply(user_query=user_review, sentiment=sentiment)

                # Insert review and response into MongoDB
                collection.insert_one({"email":st.session_state.user_email, 
                                    "review": user_review, 
                                    "reply": reply,
                                    "sentiment": sentiment,
                                    "time": datetime.now()})
                
                # Display the generated reply
                st.write(reply)

                # Send a coupon email based on sentiment
                if sentiment == "negative":
                    email_coupon(subject = "15% off on your next purchase",
                            body = "Dear Customer,you have been selected to receive a 15% discount on your next purchase. Use the code: SAVE50 at checkout.",
                            to = st.session_state.user_email)
                    
                elif sentiment == "neutral":
                    email_coupon(subject = "5% off on your next purchase",
                            body = "Dear Customer, you have been selected to receive a 5% discount on your next purchase. Use the code: SAVE25 at checkout.",
                            to = st.session_state.user_email)

        # Logout button                    
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            change_page("Home")

        
    else:
        # Prompt to log in if the user is not authenticated
        st.write("Please log in to enter a review and generate a reply.")








