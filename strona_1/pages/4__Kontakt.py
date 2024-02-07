import streamlit as st

CSS_FILE = "style/style.css"

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

