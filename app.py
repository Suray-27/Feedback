import streamlit as st
from pymongo import MongoClient
from ai_response import generate_reply
from email_utils import email_coupon 



st.title("Customer reply generator")

st.header("User Login")
user_email = st.text_input("Enter Your Email:", placeholder="eg., user@gmail.com")

if st.button("Login"):
    if (user_email == "" or "@gmail.com" not in user_email):
        st.error("Please enter a valid email.")
        st.stop()
    else:
        st.session_state.logged_in = True
        #st.session_state.user_email = user_email
        st.success("User logged in successfully.")

if st.session_state:

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
            elif sentiment == "neutral":
                email_coupon("25% off on your next purchase",
                        "Dear Customer, you have been selected to receive a 25% discount on your next purchase. Use the code: SAVE25 at checkout.",
                        "surendharbaskar3@gmail.com")



    else:
        st.write("Please log in to enter a review and generate a reply.")





