import streamlit as st

st.title("Contact Us")
topics_list = ["Job Proposals", "Enquiry", "Others"]

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address")
    topic = st.selectbox("Select the topic you want to discuss", topics_list)
    raw_message = st.text_area("Message")
    button = st.form_submit_button("Submit")
    if button:
        print("Pressed")