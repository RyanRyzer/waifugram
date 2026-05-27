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
    layout="wide",
    initial_sidebar_state="expanded"
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
    background:transparent !important;
}

/* =========================
HAMBURGER TOGGLE
========================= */

[data-testid="stSidebarNav"] {
    opacity:0;
    height:0;
}

button[kind="header"] {
    display:flex !important;
}

[data-testid="collapsedControl"] svg {
    display:none !important;
}

[data-testid="collapsedControl"]::before {

    content:"☰";

    font-size:24px;

    font-weight:700;

    color:white;

    line-height:1;
}

[data-testid="collapsedControl"] {

    position:fixed !important;

    top:14px !important;
    left:14px !important;

    width:48px !important;
    height:48px !important;

    border-radius:14px !important;

    background:
    linear-gradient(
        135deg,
        #1d4ed8,
        #2563eb
    ) !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    display:flex !important;

    align-items:center !important;

    justify-content:center !important;

    z-index:999999 !important;

    transition:0.25s ease !important;

    box-shadow:
    0 8px 25px rgba(37,99,235,0.35) !important;

    backdrop-filter:blur(10px);
}

[data-testid="collapsedControl"]:hover {

    transform:scale(1.08);

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    ) !important;

    box-shadow:
    0 0 25px rgba(59,130,246,0.55) !important;
}

/* =========================
GLOBAL
========================= */

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

/* =========================
TITLE
========================= */

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

/* =========================
CARD
========================= */

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

/* =========================
INPUT
========================= */

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

/* =========================
BUTTON
========================= */

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

/* =========================
TABS
========================= */

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

/* =========================
PROGRESS
========================= */

.stProgress > div > div {

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );
}

/* =========================
SIDEBAR BUTTON
========================= */

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

                col1, col2 = st.columns([1,2])

                with col1:

                    if os.path.exists(image_path):

                        st.image(
                            image_path,
                            width=250
                        )

                with col2:

                    st.markdown(f"""
                    <div class='card'>

                    <h1>
                    🌸 {prediction}
                    </h1>

                    <br>

                    <h3>
                    Confidence:
                    {confidence:.2f}%
                    </h3>

                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

        else:

            st.warning(
                "Belum ada history prediction"
            )

    elif menu == "About":

        st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
<style>
.main-title{
    font-size:48px;
    font-weight:bold;
    color:#4F8CFF;
    margin-bottom:20px;
}

.about-card{
    background: rgba(20,25,45,0.85);
    padding:35px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 25px rgba(0,0,0,0.25);
}

.section-title{
    font-size:32px;
    font-weight:bold;
    margin-top:25px;
    margin-bottom:15px;
    color:white;
}

.desc{
    font-size:18px;
    line-height:1.8;
    color:#E5E7EB;
}

.feature-box{
    background: rgba(255,255,255,0.04);
    padding:20px;
    border-radius:18px;
    margin-top:15px;
}

.category-tag{
    display:inline-block;
    padding:8px 18px;
    border-radius:15px;
    background:#3B82F6;
    color:white;
    margin:6px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
🌸 About Waifugram AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-card">

<div class="desc">
<b>Waifugram AI</b> merupakan sistem cerdas berbasis 
<b>Machine Learning</b> dan <b>TensorFlow Lite</b> yang dirancang untuk 
mendeteksi dan mengklasifikasikan karakter anime perempuan berdasarkan 
kategori tertentu melalui analisis gambar.

Sistem ini mampu melakukan prediksi kategori karakter anime secara otomatis 
dengan memanfaatkan model Artificial Intelligence yang telah dilatih menggunakan 
dataset gambar anime.
</div>

<div class="section-title">
🎯 Kategori Karakter
</div>

<div class="desc">
Waifugram AI dapat mendeteksi beberapa kategori karakter anime perempuan, yaitu:
</div>

<br>

<div>
<span class="category-tag">Maid</span>
<span class="category-tag">Cat Girl</span>
<span class="category-tag">Game</span>
<span class="category-tag">Milf</span>
<span class="category-tag">Loli</span>
<span class="category-tag">Furry</span>
<span class="category-tag">Teen</span>
<span class="category-tag">Elf</span>
</div>

<div class="section-title">
⚙️ Cara Kerja Sistem
</div>

<div class="feature-box">
<div class="desc">
1. User mengunggah gambar karakter anime perempuan.<br><br>

2. Sistem melakukan preprocessing gambar seperti resize dan normalisasi data gambar.<br><br>

3. Model TensorFlow Lite melakukan proses inferensi terhadap gambar input.<br><br>

4. Sistem menghitung nilai probabilitas dari setiap kategori karakter.<br><br>

5. Hasil prediksi utama akan ditampilkan beserta nilai confidence dan Top 3 kemungkinan kategori karakter anime.
</div>
</div>

<div class="section-title">
🧠 Metode Artificial Intelligence
</div>

<div class="feature-box">
<div class="desc">
Waifugram AI menggunakan metode <b>Deep Learning</b> berbasis 
<b>Convolutional Neural Network (CNN)</b> yang dioptimasi menggunakan 
<b>TensorFlow Lite</b> agar proses prediksi dapat berjalan lebih cepat dan ringan.

Model CNN digunakan karena sangat efektif dalam mengenali pola visual, 
fitur wajah, atribut pakaian, bentuk telinga, warna rambut, serta elemen visual 
lain yang umum ditemukan pada karakter anime.
</div>
</div>

<div class="section-title">
💻 Teknologi yang Digunakan
</div>

<div class="feature-box">
<div class="desc">
• Streamlit → Framework antarmuka web interaktif berbasis Python<br>
• TensorFlow Lite → Engine Machine Learning untuk inferensi model AI<br>
• NumPy → Pengolahan data numerik dan array<br>
• Pillow → Pemrosesan gambar<br>
• SQLite → Penyimpanan data user dan riwayat prediksi<br>
• Python → Bahasa pemrograman utama sistem
</div>
</div>

<div class="section-title">
✨ Fitur Utama
</div>

<div class="feature-box">
<div class="desc">
• Login dan Register User<br>
• Dashboard Interaktif<br>
• Upload Gambar Anime<br>
• AI Character Detection<br>
• Confidence Score Prediction<br>
• Top 3 Prediction Result<br>
• Prediction History<br>
• Modern User Interface<br>
• Real-time Image Classification
</div>
</div>

<div class="section-title">
🚀 Tujuan Sistem
</div>

<div class="feature-box">
<div class="desc">
Waifugram AI dikembangkan sebagai implementasi sistem cerdas berbasis 
Machine Learning untuk melakukan klasifikasi gambar anime secara otomatis 
dengan antarmuka yang modern, interaktif, dan mudah digunakan.
</div>
</div>

</div>
""", unsafe_allow_html=True)
