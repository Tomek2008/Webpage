import streamlit as st

CSS_FILE = "style/style.css"


st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:")

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Witaj")
st.header("Witaj")
st.subheader("Witaj")
st.write("Witaj")



