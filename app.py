import streamlit as st
from pymongo import MongoClient
from ai_response import generate_reply
from email_utils import email_coupon 

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/<feedback_db>")
db = client["feedback_db"]
collection = db["reviews"]

st.title("Customer reply generator")

st.sidebar.header("User Login")
user_email = st.sidebar.text_input("Enter Your Email:", placeholder="eg., user@gmail.com")

if st.sidebar.button("Login"):
    if not user_email.strip():
        st.sidebar.error("Please enter a valid email.")
    else:
        if not collection.find_one({"user_email": user_email}):
            collection.insert_one({"user_email": user_email})
            st.sidebar.success("User logged in successfully.")

user_review = st.text_area("Enter Your Review:",placeholder="Write your review here...")
sentiment = st.selectbox("Select Sentiment", ["positive", "negative","neutral"])

if st.button("Generate Reply"):
    if not user_review.strip():
        st.error("Please enter a review.")
        st.stop()
    else:
        reply = generate_reply(user_query=user_review, sentiment=sentiment)
        st.write(reply)

    if sentiment == "negative":
        email_coupon("50% off on your next purchase",
                     "Dear Customer,you have been selected to receive a 50% discount on your next purchase. Use the code: SAVE50 at checkout.",
                     "yyin42171@gmail.com")

    # Save the review and reply to MongoDB
    collection.insert_one({"review": user_review, "reply": reply, "sentiment": sentiment})
    st.success("Reply generated and saved to MongoDB.")

else:
    st.write("Please a enter a review and select a sentiment to generate a reply.")





