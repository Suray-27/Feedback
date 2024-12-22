import os
from datetime import datetime
import streamlit as st
from pymongo import MongoClient
from ai_response import generate_reply
from email_utils import email_coupon 

client = MongoClient(os.getenv("MONGODB_PASSWORD"))
db = client["feedback_db"]
collection = db["reviews"]

st.set_page_config(page_title="Auto-Navigation App", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None


def change_page(new_page):
    st.session_state.page = new_page

if st.session_state.page == "Home":
    st.title("Customer reply generator")
    st.header("User Login")

    user_email = st.text_input("Enter Your Email:", placeholder="eg., user@gmail.com")

    if st.button("Login"):
        if user_email.endswith("@gmail.com") and user_email != "":
            #user_data = collection.find_one({"email":user_email})
            #if not user_data:
                #collection.insert_one({"email":user_email})
            st.session_state.logged_in = True
            st.session_state.user_email = user_email
            st.success("User logged in successfully.")
            change_page("User Reviews")
        else:
            st.error("Please enter a valid email address.")

elif st.session_state.page == "User Reviews":
    st.title("Customer Reviews")

    if st.session_state.logged_in:
        user_review = st.text_area("Enter Your Review:",placeholder="Write your review here...")
        sentiment = st.selectbox("Select Sentiment", ["positive", "negative","neutral"])

        if st.button("Generate Reply"):
            if not user_review.strip():
                st.error("Please enter a review.")
                st.stop()
            else:
                reply = generate_reply(user_query=user_review, sentiment=sentiment)

                collection.insert_one({"email":st.session_state.user_email, 
                                    "review": user_review, 
                                    "reply": reply,
                                    "sentiment": sentiment,
                                    "time": datetime.now()})
                st.write(reply)

                if sentiment == "negative":
                    email_coupon(subject = "15% off on your next purchase",
                            body = "Dear Customer,you have been selected to receive a 15% discount on your next purchase. Use the code: SAVE50 at checkout.",
                            to = st.session_state.user_email)
                    
                elif sentiment == "neutral":
                    email_coupon(subject = "5% off on your next purchase",
                            body = "Dear Customer, you have been selected to receive a 5% discount on your next purchase. Use the code: SAVE25 at checkout.",
                            to = st.session_state.user_email)
                    
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            change_page("Home")

        
    else:
        st.write("Please log in to enter a review and generate a reply.")








