import streamlit as st
import joblib
import numpy as np
import base64
from utils.logout import sidebar_logout
from utils.custom_sidebar import custom_sidebar

# ---- Page Config ----
st.set_page_config(page_title="Breast Cancer Predictor", page_icon="🎗️")
custom_sidebar()

# ---- Sidebar Styling ----
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] { display: none; }
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

# ---- Background ----
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
                Please <b>log in</b> to access the Breast Cancer Predictor.<br>
                Use the sidebar to log in and try again.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔐 Go to Login Page"):
            st.switch_page("pages/Login.py")
    st.stop()

# ---- Load Model and Scaler ----
st.title("🎀 Breast Cancer Risk Prediction")
st.markdown("### Enter the diagnostic measurements below:")

try:
    model = joblib.load("breast_cancer_model.pkl")
    scaler = joblib.load("breast_cancer_scaler.pkl")
except Exception as e:
    st.error(f"❌ Error loading model or scaler: {e}")
    st.stop()

# ---- 30 Input Features Grouped ----
input_values = []

mean_features = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean"
]

se_features = [
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se",
    "compactness_se", "concavity_se", "concave points_se", "symmetry_se", "fractal_dimension_se"
]

worst_features = [
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

with st.expander("🔍 Mean Features"):
    for feature in mean_features:
        val = st.number_input(feature.replace("_", " ").title(), format="%.4f")
        input_values.append(val)

with st.expander("📏 Standard Error Features"):
    for feature in se_features:
        val = st.number_input(feature.replace("_", " ").title(), format="%.4f")
        input_values.append(val)

with st.expander("🚨 Worst Features"):
    for feature in worst_features:
        val = st.number_input(feature.replace("_", " ").title(), format="%.4f")
        input_values.append(val)

# ---- Prediction Button ----
if st.button("🔮 Predict"):
    try:
        input_data = np.array([input_values])
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)

        if prediction[0] == 1:
            st.error("⚠️ High Risk of Breast Cancer")
        else:
            st.success("✅ Low Risk of Breast Cancer")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
