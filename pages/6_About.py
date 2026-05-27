import streamlit as st

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
