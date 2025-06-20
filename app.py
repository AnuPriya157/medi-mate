import streamlit as st
import os
import base64
import random
from streamlit_autorefresh import st_autorefresh

# ---- CONFIG ----
st.set_page_config(page_title="MediMate", page_icon="💙", layout="centered")
st_autorefresh(interval=10000, key="auto-refresh")

# ---- SESSION ----
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ---- CSS STYLING ----
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
    .feature-card {
        background-color: #B497BD;
        color: white;
        border-radius: 12px;
        padding: 12px;
        margin: 8px 0;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        height: 110px;
        position: relative;
        transition: all 0.3s ease-in-out;
        overflow: hidden;
        font-family: 'Segoe UI', sans-serif;
    }
    .feature-card:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 14px rgba(0,0,0,0.2);
    }
    .feature-title {
        font-size: 14px;
        font-weight: 600;
        margin-top: 4px;
    }
    .feature-icon {
        font-size: 20px;
    }
    .feature-desc {
        opacity: 0;
        transition: opacity 0.4s ease-in-out;
        position: absolute;
        bottom: 8px;
        left: 6px;
        right: 6px;
        font-size: 11px;
        color: #f0f0f0;
    }
    .feature-card:hover .feature-desc {
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# ---- TITLE & GREETING ----
st.markdown('<div class="main-title">💙 Welcome to MediMate</div>', unsafe_allow_html=True)
if st.session_state["authenticated"]:
    st.markdown(f"<p style='text-align:center;'>👋 Hello, <b>{st.session_state['username']}</b>!</p>", unsafe_allow_html=True)
else:
    st.info("🔐 Please log in to access prediction features.")

# ---- MOTIVATIONAL QUOTE ----
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

# ---- HEALTH TIP ROTATOR ----
tips = [
    "🥗 Eat a balanced diet every day!",
    "🚶 Walk 30 minutes daily for a healthier life.",
    "💧 Drink at least 8 glasses of water.",
    "🧘 Practice breathing or meditation for mental health.",
    "🩺 Regular checkups = early detection!",
    "😴 Sleep 7–9 hours to recharge your body."
]
st.markdown(f"<div class='health-tip'>💡 Health Tip: <i>{random.choice(tips)}</i></div>", unsafe_allow_html=True)

# ---- PREDICTOR BUTTONS ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🩺 Diabetes Predictor"):
            st.switch_page("pages/Diabetes_Predictor.py")
    with col_b:
        if st.button("🎗️ Breast Cancer Check"):
            st.switch_page("pages/Breast_Cancer_Predictor.py")

# ---- WHY MEDIMATE ----
# ---- WHY MEDIMATE (Styled Glow Icon Cards) ----
st.markdown("""
<style>
.feature-card {
    background-color: #F4C2C2;  /* Soft pink */
    color: #2D2D2D;
    border-radius: 12px;
    padding: 12px;
    margin: 8px 0;
    text-align: center;
    box-shadow: 0 0 10px #F4C2C2;
    height: 110px;
    position: relative;
    transition: all 0.3s ease-in-out;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}
.feature-card:hover {
    background-color: #B497BD;  /* Lavender on hover */
    color: #1A1A1A;
    transform: scale(1.03);
    box-shadow: 0 0 18px #B497BD, 0 0 28px #B497BD;
}
.feature-title {
    font-size: 14px;
    font-weight: 600;
    margin-top: 4px;
}
.feature-icon {
    font-size: 20px;
}
.feature-desc {
    opacity: 0;
    transition: opacity 0.4s ease-in-out;
    position: absolute;
    bottom: 8px;
    left: 6px;
    right: 6px;
    font-size: 11px;
    color: #1A1A1A;
}
.feature-card:hover .feature-desc {
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(3)

features = [
    ("🔒", "Secure Login", "Only you can access your predictions"),
    ("📊", "Accurate Prediction", "Powered by ML for best accuracy"),
    ("🧠", "User-Friendly UI", "Simple and smooth to use"),
    ("💡", "Smart Tips", "Helpful health tips every 10 sec"),
    ("📱", "Mobile Friendly", "Easy use on phone or tablet"),
    ("🩺", "Early Detection", "Catch issues before they grow")
]

for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f'''
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        ''', unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("---")
st.markdown("<center>✨ Powered by MediMate • Predict. Prevent. Protect.</center>", unsafe_allow_html=True)

# ---- LOGOUT ----
if st.session_state["authenticated"]:
    if st.sidebar.button("🚪 Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.sidebar.success("You have been logged out.")
