import streamlit as st
from utils.logout import sidebar_logout

def custom_sidebar():
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
    .sidebar-link {
        padding: 12px 20px;
        display: block;
        text-decoration: none;
        border-radius: 8px;
        margin-bottom: 8px;
        transition: all 0.3s ease-in-out;
    }
    .sidebar-link:hover {
    background: linear-gradient(to right, #fdd835, #f06292); /* vibrant yellow to pink */
    color: #000 !important;
    font-weight: 800;
    border: 2px solid #fff;
    box-shadow: 0 0 10px #fdd835, 0 0 20px #f06292;
    transform: scale(1.07);
    transition: 0.25s ease-in-out;
}

    .sidebar-section {
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("## 🧭 Navigation", unsafe_allow_html=True)

        st.page_link("HOME.py", label=" Home", icon="🏠")
        st.page_link("pages/Breast_Cancer_Predictor.py", label=" Breast Cancer Predictor", icon="🎗️")
        st.page_link("pages/Diabetes_Predictor.py", label=" Diabetes Predictor", icon="🩺")

        if not st.session_state.get("authenticated", False):
            st.page_link("pages/Login.py", label=" Login", icon="🔑")
            st.page_link("pages/Signup.py", label=" Signup", icon="📝")

        # Floating logout (only if logged in)
        if st.session_state.get("authenticated", False):
            sidebar_logout()
