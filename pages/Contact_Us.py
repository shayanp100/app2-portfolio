import streamlit as st

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Email")
    message = st.text_area("Your Message")
    button = st.form_submit_button()
    if button:
        message = message + "\n" + user_email
        