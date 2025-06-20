import streamlit as st
import numpy as np
import joblib
import base64
from utils.logout import sidebar_logout
from utils.custom_sidebar import custom_sidebar

# ---- Page Config ----
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺")
custom_sidebar()

# ---- Hide Default Navigation ----
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar & Button Styling ----
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

# ---- Background Image ----
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

# ---- Login Protection ----
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    with open("assets/login1.gif", "rb") as f:
        gif_data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <div style='text-align:center; margin-top:30px;'>
            <img src="data:image/gif;base64,{gif_data}" alt="access denied" style="width:220px; border-radius:12px;" />
        </div>
        <div style="background: linear-gradient(to right, #fce4ec, #f3e5f5);
                    padding: 30px 25px; border-radius: 15px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    margin-top: 20px; text-align: center;">
            <div style="font-size: 28px; color: #6A1B9A; margin-bottom: 10px;">🔐 Access Denied</div>
            <div style="font-size: 16px; color: #444;">
                Please <b>log in</b> to access the Diabetes Predictor.<br>
                Click the button below to go to the login page.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ✅ Center the button properly
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔑 Go to Login Page"):
            st.switch_page("pages/Login.py")

    st.stop()


# ---- Load Model and Scaler ----
try:
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("diabetes_scaler.pkl")
except Exception as e:
    st.error(f"❌ Error loading model or scaler: {e}")
    st.stop()

# ---- UI Layout ----
st.title("🩺 Diabetes Risk Predictor")
st.markdown("### Enter your health parameters:")

# ---- User Inputs ----
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=1000, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# ---- Predict ----
if st.button("🧠 Predict"):
    try:
        input_data = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠️ You are at risk of Diabetes.")
        else:
            st.success("✅ You are not at risk of Diabetes.")
    except Exception as e:
        st.error(f"Prediction error: {e}")
