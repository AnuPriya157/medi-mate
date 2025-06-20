import streamlit as st
import os
import base64
import random
from utils.logout import sidebar_logout
from utils.custom_sidebar import custom_sidebar




# ---- CONFIG ----
st.set_page_config(page_title="MediMate", page_icon="💙", layout="centered")
st.markdown("""
    <style>
    /* Hide default Streamlit sidebar navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)


# ---- BACKGROUND ----
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        b64 = base64.b64encode(img.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

set_bg_from_local("assets/background1.jpg")

# ---- SESSION STATE ----
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ---- GLOBAL CSS ----
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 10px;
    }
    .quote {
        font-style: italic;
        font-size: 1.1rem;
        color: #6a1b9a;
        text-align: center;
        margin-bottom: 15px;
    }
    .health-tip {
        background: linear-gradient(to right, #e3f2fd, #fff8e1);
        padding: 12px;
        border-radius: 10px;
        font-size: 1.05rem;
        text-align: center;
        color: #37474f;
        margin-bottom: 25px;
        border-left: 6px solid #42a5f5;
    }
    div.stButton > button {
        background-color: #F4C2C2;
        color: #2D2D2D;
        border: none;
        padding: 14px 24px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 16px;
        box-shadow: 0 0 10px #F4C2C2;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #B497BD;
        box-shadow: 0 0 18px #B497BD, 0 0 28px #B497BD;
        transform: scale(1.05);
        color: #1A1A1A;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #5DC1B9, #3498DB);
        color: white;
        backdrop-filter: blur(6px);
        border-right: 2px solid #4FA6CA;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebarNav"] a {
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s ease-in-out;
    }
    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(255, 255, 255, 0.15);
        color: #ffffff !important;
        transform: scale(1.05);
        font-weight: 600;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown('<div class="main-title">💙 Welcome to MediMate</div>', unsafe_allow_html=True)
if st.session_state["authenticated"]:
    st.markdown(f"<p style='text-align:center;'>👋 Hello, <b>{st.session_state['username']}</b>!</p>", unsafe_allow_html=True)
else:
    st.info("🔐 Please log in to access prediction features.")

# ---- QUOTE ----
quote = random.choice([
    "“Your health is your wealth.” 💎",
    "“Prevention is better than cure.” 💡",
    "“Take care of your body. It’s the only place you have to live.” 💚"
])
st.markdown(f"<div class='quote'>{quote}</div>", unsafe_allow_html=True)

# ---- BANNER ----
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

banner_path = "assets/Banner.png"
if os.path.exists(banner_path):
    encoded_banner = get_base64_image(banner_path)
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{encoded_banner}' style='width: 150px; object-fit: contain;' />
        </div>
    """, unsafe_allow_html=True)

# ---- TIP ROTATOR ----
tips = [
    "🥗 Eat a balanced diet every day!",
    "🚶 Walk 30 minutes daily for a healthier life.",
    "💧 Drink at least 8 glasses of water.",
    "🧘 Practice breathing or meditation for mental health.",
    "🦥 Regular checkups = early detection!",
    "🛌 Sleep 7–9 hours to recharge your body."
]
st.markdown(f"<div class='health-tip'>💡 Health Tip: <i>{random.choice(tips)}</i></div>", unsafe_allow_html=True)

# ---- PREDICTION BUTTONS ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🦥 Diabetes Predictor"):
            st.switch_page("Diabetes_Predictor.py")
    with col_b:
        if st.button("🎗️ Breast Cancer Check"):
            st.switch_page("Breast_Cancer_Predictor.py")

# ---- ICON CARDS ----
st.markdown("""
<style>
.icon-wrapper {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 25px;
    margin: 50px 0;
}
.card {
    position: relative;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 25px 15px;
    width: 220px;
    height: 240px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    color: #000;
    flex: 1 1 200px;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
}
.card-icon {
    font-size: 36px;
    background: #ffffff33;
    padding: 12px;
    border-radius: 50%;
    margin-bottom: 10px;
    display: inline-block;
}
.card-label {
    font-size: 15px;
    font-weight: bold;
    margin-bottom: 6px;
}
.card-desc {
    font-size: 13px;
    color: #2d2d2d;
    margin-bottom: 6px;
}
.card-tooltip {
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s;
    position: absolute;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    background: #333;
    color: #fff;
    font-size: 12px;
    padding: 10px;
    border-radius: 10px;
    text-align: left;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
}
.card:hover .card-tooltip {
    visibility: visible;
    opacity: 1;
}
</style>

<div class="icon-wrapper">

  <div class="card">
    <div class="card-icon">🔐</div>
    <div class="card-label">Secure Login</div>
    <div class="card-desc">Sign in safely with your credentials.</div>
    <div class="card-tooltip">
        • Session tracking<br>
        • Role-based access<br>
        • Logout anytime securely
    </div>
  </div>

  <div class="card">
    <div class="card-icon">🩺</div>
    <div class="card-label">Diabetes Predictor</div>
    <div class="card-desc">Check your diabetes risk easily.</div>
    <div class="card-tooltip">
        • Uses ML model<br>
        • Accurate medical inputs<br>
        • Fast results display
    </div>
  </div>

  <div class="card">
    <div class="card-icon">🎗️</div>
    <div class="card-label">Cancer Check</div>
    <div class="card-desc">Early-stage breast cancer prediction.</div>
    <div class="card-tooltip">
        • Based on real data<br>
        • Lightweight & efficient<br>
        • No patient data stored
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("---")
st.markdown("<center>✨ Powered by MediMate • Predict. Prevent. Protect.</center>", unsafe_allow_html=True)



# Show sidebar logout button (only if logged in)
custom_sidebar()
sidebar_logout()


