import streamlit as st

st.set_page_config(page_title="Dashboard")

st.title("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Prediction", "152")

with col2:
    st.metric("Total Users", "38")

with col3:
    st.metric("Accuracy", "89%")

st.subheader("🔥 Popular Categories")

st.progress(90)
st.write("Cat Girl")

st.progress(75)
st.write("Elf")

st.progress(60)
st.write("Maid")