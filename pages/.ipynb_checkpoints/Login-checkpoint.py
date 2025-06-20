import streamlit as st
import json
import os
from utils.custom_sidebar import custom_sidebar



st.set_page_config(page_title="Login", page_icon="🔐")
custom_sidebar()
st.markdown("""
    <style>
    /* Hide default Streamlit sidebar navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #5DC1B9, #3498DB);
        color: white;
        backdrop-filter: blur(6px);
        border-right: 2px solid #4FA6CA;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Sidebar nav item hover effect */
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
st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

import base64

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

# Load users
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# ---- Login Interface ----
st.title("🔐 Login to MediMate")

username = st.text_input("Enter Username").strip()
password = st.text_input("Enter Password", type="password").strip()

# ---- Check login on button click ----
if st.button("Login"):
    users = load_users()

    if username in users:
        if users[username]["password"] == password:
            st.success(f"✅ Welcome back, {username}!")
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.switch_page("HOME.py")
        else:
            st.error("❌ Incorrect password. Please try again.")
    else:
        st.error("❌ Username does not exist. Please sign up first.")

