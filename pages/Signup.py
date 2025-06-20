import streamlit as st
import json
import os
from utils.custom_sidebar import custom_sidebar


st.set_page_config(page_title="Signup", page_icon="📝")
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
            return json.load(f)
    return {}

# Save new user
def save_user(user_data):
    users = load_users()
    if user_data["username"] in users:
        return False
    users[user_data["username"]] = user_data
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)
    return True

st.title("📝 Create Your Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", ["Select", "Female", "Male", "Other"])

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Signup"):
        if not all([name, email, phone, username, password]) or gender == "Select":
            st.error("❌ Please fill in all the fields.")
        else:
            user_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "username": username,
                "password": password,
                "age": age,
                "gender": gender
            }
            if save_user(user_data):
                st.success("✅ Account created successfully! You can now log in.")
            else:
                st.warning("⚠️ Username already exists.")

