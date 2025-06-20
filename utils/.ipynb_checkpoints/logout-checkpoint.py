# utils/logout.py
import streamlit as st
import time

def sidebar_logout():
    if st.session_state.get("authenticated", False):
        st.markdown("""
        <style>
        .custom-logout-button {
            background-color: #F4C2C2;
            color: #2D2D2D;
            padding: 12px 24px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 16px;
            margin-top: 30px;
            border: none;
            cursor: pointer;
            box-shadow: 0 0 10px #F4C2C2;
            transition: 0.3s ease;
        }
        .custom-logout-button:hover {
            background-color: #B497BD;
            box-shadow: 0 0 18px #B497BD;
            transform: scale(1.05);
            color: #1A1A1A;
        }
        </style>
        """, unsafe_allow_html=True)

        # Button in sidebar with styling
        if st.sidebar.button("🚪 Logout", key="logout_btn"):
            st.session_state.clear()
            st.success("Logging Out...")
            time.sleep(1.5)
            st.switch_page("Home.py")
