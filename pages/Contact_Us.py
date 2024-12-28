import pandas as pd
import streamlit as st
from send_email import  send_email

st.title("Contact Us")
topics = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address")
    topic = st.selectbox("Select the topic you want to discuss", topics["topic"])
    raw_message = st.text_area("Message")
    message = f"""\
Subject: Company Website

From: {user_email}

Topic: {topic}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email send successfully")