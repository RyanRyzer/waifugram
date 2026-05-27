import streamlit as st
from utils.auth import login_user

st.set_page_config(page_title="Login")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #141421, #202040);
}

.login-box {
    background:#1f1f35;
    padding:40px;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

st.title("🔐 Login")

with st.container():

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if login_user(username, password):
            st.success("Login berhasil")
        else:
            st.error("Username atau password salah")