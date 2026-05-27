import streamlit as st
from utils.auth import register_user

st.set_page_config(page_title="Register")

st.title("📝 Register")

username = st.text_input("Username")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

confirm = st.text_input(
    "Confirm Password",
    type="password"
)

if st.button("Register"):

    if password != confirm:
        st.error("Password tidak sama")

    else:

        register_user(
            username,
            email,
            password
        )

        st.success("Register berhasil")