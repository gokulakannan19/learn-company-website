import streamlit as st
from send_email import  send_email

st.title("Contact Us")
topics_list = ["Job Proposals", "Enquiry", "Others"]

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address")
    topic = st.selectbox("Select the topic you want to discuss", topics_list)
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