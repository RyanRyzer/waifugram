import os
import uuid

import streamlit as st

from PIL import Image

from utils.auth import (
    register_user,
    login_user
)

from utils.database import (
    cursor,
    conn
)

from utils.prediction import (
    predict_image,
    labels
)

st.set_page_config(
    page_title="Waifugram AI",
    page_icon="🌸",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

st.markdown("""
<style>

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    visibility:hidden;
}

[data-testid="stSidebarNav"] {
    display:none;
}

.stApp {

    background:
    linear-gradient(
        135deg,
        #050816,
        #0f172a,
        #111827
    );

    color:white;
}

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #0b1120,
        #111827
    );

    border-right:
    1px solid rgba(255,255,255,0.05);

    min-width:320px;
}

section[data-testid="stSidebar"] * {
    color:white;
}

.sidebar-title {

    text-align:center;

    font-size:38px;

    font-weight:bold;

    color:#60a5fa;

    margin-top:15px;

    margin-bottom:20px;
}

.main-title {

    text-align:center;

    font-size:65px;

    font-weight:bold;

    background:
    linear-gradient(
        90deg,
        #60a5fa,
        #3b82f6,
        #ffffff
    );

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;

    margin-bottom:10px;
}

.sub-title {

    text-align:center;

    color:#d1d5db;

    font-size:18px;

    margin-bottom:40px;
}

.auth-card {

    background:
    rgba(255,255,255,0.04);

    backdrop-filter:blur(12px);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius:24px;

    padding:40px;

    box-shadow:
    0 0 40px rgba(0,0,0,0.25);
}

.card {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius:24px;

    padding:25px;

    margin-bottom:20px;

    backdrop-filter:blur(10px);
}

.metric-card {

    background:
    rgba(255,255,255,0.04);

    border-radius:22px;

    padding:30px;

    text-align:center;

    border:
    1px solid rgba(255,255,255,0.06);

    transition:0.3s;
}

.metric-card:hover {

    transform:translateY(-5px);

    box-shadow:
    0 0 30px rgba(59,130,246,0.15);
}

.stTextInput input {

    background:#0f172a !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    color:white !important;

    border-radius:14px !important;

    padding:14px !important;
}

.stTextInput label {
    color:white !important;
}

.stButton > button {

    width:100%;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );

    color:white;

    border:none;

    border-radius:14px;

    padding:14px;

    font-weight:bold;

    transition:0.3s;
}

.stButton > button:hover {

    transform:translateY(-2px);

    box-shadow:
    0 0 25px rgba(59,130,246,0.35);
}

div[data-baseweb="tab-list"] {

    gap:20px;
}

button[data-baseweb="tab"] {

    background:
    rgba(255,255,255,0.04);

    border-radius:14px;

    padding:10px 20px;

    color:white;
}

button[data-baseweb="tab"][aria-selected="true"] {

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );
}

.stProgress > div > div {

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );
}

.sidebar-btn button {

    width:100% !important;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:16px !important;

    padding:14px !important;

    margin-bottom:14px !important;

    font-weight:600 !important;

    font-size:16px !important;

    transition:0.3s !important;

    box-shadow:
    0 4px 20px rgba(37,99,235,0.20);
}

.sidebar-btn button:hover {

    transform:translateX(6px);

    background:
    linear-gradient(
        90deg,
        #1d4ed8,
        #2563eb
    ) !important;

    box-shadow:
    0 0 25px rgba(37,99,235,0.40);
}

</style>
""", unsafe_allow_html=True)

if not st.session_state.logged_in:

    st.query_params.clear()

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        display:none;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='main-title'>
        🌸 Waifugram AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub-title'>
        AI Anime Character Detection System
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1.2,1])

    with col2:

        st.markdown("""
        <div class='auth-card'>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs([
            "🔐 Login",
            "📝 Register"
        ])

        with tab1:

            login_username = st.text_input(
                "Username",
                key="login_user"
            )

            login_password = st.text_input(
                "Password",
                type="password",
                key="login_pass"
            )

            if st.button("Login"):

                success = login_user(
                    login_username,
                    login_password
                )

                if success:

                    st.session_state.logged_in = True

                    st.session_state.username = (
                        login_username
                    )

                    st.rerun()

                else:
                    st.error(
                        "Username atau password salah"
                    )

        with tab2:

            reg_username = st.text_input(
                "Username",
                key="reg_user"
            )

            reg_email = st.text_input(
                "Email"
            )

            reg_password = st.text_input(
                "Password",
                type="password"
            )

            reg_confirm = st.text_input(
                "Confirm Password",
                type="password"
            )

            if st.button("Create Account"):

                if reg_password != reg_confirm:

                    st.error(
                        "Password tidak sama"
                    )

                else:

                    success = register_user(
                        reg_username,
                        reg_email,
                        reg_password
                    )

                    if success:

                        st.session_state.logged_in = True

                        st.session_state.username = (
                            reg_username
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Username sudah digunakan"
                        )

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

else:

    st.sidebar.markdown("""
    <div class='sidebar-title'>
        🌸 Waifugram
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <hr style='
    border:1px solid rgba(255,255,255,0.08);
    margin-top:-10px;
    margin-bottom:25px;
    '>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <h3 style='
    color:white;
    margin-bottom:20px;
    '>
    🚀 Navigation
    </h3>
    """, unsafe_allow_html=True)

    with st.sidebar:

        st.markdown("<div class='sidebar-btn'>", unsafe_allow_html=True)
        if st.button("🏠 Dashboard"):
            st.session_state.menu = "Dashboard"
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='sidebar-btn'>", unsafe_allow_html=True)
        if st.button("🤖 AI Detection"):
            st.session_state.menu = "AI Detection"
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='sidebar-btn'>", unsafe_allow_html=True)
        if st.button("📜 History"):
            st.session_state.menu = "History"
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='sidebar-btn'>", unsafe_allow_html=True)
        if st.button("ℹ️ About"):
            st.session_state.menu = "About"
        st.markdown("</div>", unsafe_allow_html=True)

    menu = st.session_state.menu

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    st.sidebar.markdown(f"""
    <div style='
    background:rgba(255,255,255,0.05);
    padding:16px;
    border-radius:16px;
    margin-top:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.06);
    '>
    👤 Login sebagai:
    <br><br>
    <b>{st.session_state.username}</b>
    </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.rerun()

    if menu == "Dashboard":

        st.markdown("""
        <div class='main-title'>
            📊 Dashboard
        </div>
        """, unsafe_allow_html=True)

        cursor.execute(
            "SELECT COUNT(*) FROM history"
        )

        total_prediction = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM users"
        )

        total_users = cursor.fetchone()[0]

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(f"""
            <div class='metric-card'>
                <h1>{total_prediction}</h1>
                <p>Total Prediction</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class='metric-card'>
                <h1>{total_users}</h1>
                <p>Total Users</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:

            st.markdown(f"""
            <div class='metric-card'>
                <h1>TensorFlow Lite</h1>
                <p>AI Model</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
            <h2>🔥 Available Categories</h2>
        </div>
        """, unsafe_allow_html=True)

        for category in labels:

            st.write(category)

            st.progress(75)

    elif menu == "AI Detection":

        st.markdown("""
        <div class='main-title'>
            🤖 AI Detection
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
            <h3>
                Upload Anime Image
            </h3>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file:

            image = Image.open(
                uploaded_file
            ).convert("RGB")

            col1, col2, col3 = st.columns([1,2,1])

            with col2:

                st.image(
                    image,
                    width=400
                )

            label, confidence, output = (
                predict_image(image)
            )

            st.markdown("""
            <div class='card'>
            """, unsafe_allow_html=True)

            st.success(
                f"Prediction: {label}"
            )

            st.info(
                f"Confidence: {confidence:.2f}%"
            )

            st.subheader(
                "Top Predictions"
            )

            for i in range(len(output)):

                score = (
                    float(output[i]) * 100
                )

                st.write(
                    f"{labels[i]} - {score:.2f}%"
                )

                st.progress(
                    min(int(score), 100)
                )

            st.markdown("""
            </div>
            """, unsafe_allow_html=True)

            if not os.path.exists("uploads"):
                os.makedirs("uploads")

            filename = (
                str(uuid.uuid4()) + ".png"
            )

            filepath = os.path.join(
                "uploads",
                filename
            )

            image.save(filepath)

            cursor.execute(
                """
                INSERT INTO history
                (
                    username,
                    prediction,
                    confidence,
                    image_path
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    st.session_state.username,
                    label,
                    confidence,
                    filepath
                )
            )

            conn.commit()

    elif menu == "History":

        st.markdown("""
        <div class='main-title'>
            📜 History
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='sub-title'>
            Your Previous AI Predictions
        </div>
        """, unsafe_allow_html=True)

        cursor.execute(
            """
            SELECT prediction,
                   confidence,
                   image_path
            FROM history
            WHERE username=?
            ORDER BY id DESC
            """,
            (
                st.session_state.username,
            )
        )

        rows = cursor.fetchall()

        if rows:

            for row in rows:

                prediction = row[0]

                confidence = row[1]

                image_path = row[2]

                st.markdown("""
                <div style='margin-bottom:25px;'>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns([1,2])

                with col1:

                    if os.path.exists(image_path):

                        st.image(
                            image_path,
                            width=250
                        )

                with col2:

                    st.markdown(f"""
                    <div style='
                    background:rgba(255,255,255,0.04);
                    border:1px solid rgba(255,255,255,0.06);
                    border-radius:24px;
                    padding:35px;
                    min-height:250px;
                    backdrop-filter:blur(10px);
                    display:flex;
                    flex-direction:column;
                    justify-content:center;
                    '>

                    <h1 style='
                    color:white;
                    margin-bottom:20px;
                    font-size:42px;
                    '>
                    🌸 {prediction}
                    </h1>

                    <div style='
                    margin-top:10px;
                    margin-bottom:15px;
                    '>

                    <span style='
                    font-size:18px;
                    color:#cbd5e1;
                    '>
                    Confidence Score
                    </span>

                    </div>

                    <div style='
                    width:100%;
                    height:18px;
                    background:rgba(255,255,255,0.08);
                    border-radius:30px;
                    overflow:hidden;
                    margin-bottom:15px;
                    '>

                        <div style='
                        width:{confidence}%;
                        height:100%;
                        background:
                        linear-gradient(
                            90deg,
                            #2563eb,
                            #60a5fa
                        );
                        border-radius:30px;
                        '>
                        </div>

                    </div>

                    <h2 style='
                    color:#60a5fa;
                    margin-top:5px;
                    '>
                    {confidence:.2f}%
                    </h2>

                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("""
                </div>
                """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div style='
            background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.06);
            border-radius:24px;
            padding:60px;
            text-align:center;
            margin-top:40px;
            '>

            <h1 style='font-size:70px;'>
            📂
            </h1>

            <h2 style='color:white;'>
            No Prediction History
            </h2>

            <p style='
            color:#cbd5e1;
            margin-top:10px;
            font-size:18px;
            '>
            Upload anime images first
            to see prediction history here.
            </p>

            </div>
            """, unsafe_allow_html=True)

    elif menu == "About":

        st.markdown("""
        <div class='main-title'>
            ℹ️ About
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>

        ## 🌸 Waifugram AI

        Waifugram AI adalah sistem
        cerdas berbasis machine learning
        untuk mendeteksi kategori
        karakter anime menggunakan
        TensorFlow Lite.

        ### Teknologi
        - Streamlit
        - TensorFlow Lite
        - SQLite
        - Python
        - NumPy
        - Pillow

        ### Fitur
        - Login & Register
        - Dashboard
        - AI Detection
        - Prediction History
        - Modern UI
        - Real-time Prediction

        </div>
        """, unsafe_allow_html=True)