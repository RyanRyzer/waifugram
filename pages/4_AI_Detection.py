import streamlit as st
from PIL import Image
from utils.prediction import predict_image
from utils.database import cursor, conn

st.set_page_config(page_title="AI Detection")

st.title("🌸 AI Waifu Detection")

uploaded_file = st.file_uploader(
    "Upload Anime Image",
    type=['jpg', 'jpeg', 'png']
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        use_container_width=True
    )

    label, confidence, output = predict_image(image)

    st.success(f"Prediction: {label}")

    st.info(f"Confidence: {confidence:.2f}%")

    st.subheader("Top Predictions")

    categories = [
        "Maid",
        "Cat Girl",
        "Elf",
        "Furry",
        "Loli",
        "Game",
        "Teen",
        "Milf"
    ]

    for i in range(len(categories)):

        score = float(output[i]) * 100

        st.write(f"{categories[i]} - {score:.2f}%")

        st.progress(min(int(score), 100))