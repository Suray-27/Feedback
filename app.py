import streamlit as st
from ai_response import generate_reply

st.title("Customer reply generator")

user_review = st.text_area("Enter Your Review:")
sentiment = st.selectbox("Select Sentiment", ["positive", "negative","neutral"])

if st.button("Generate Reply"):
    reply = generate_reply(user_query=user_review, sentiment=sentiment)
    st.write(reply)
else:
    st.write("Please a enter a review and select a sentiment to generate a reply.")




