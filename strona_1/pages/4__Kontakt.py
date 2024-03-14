import streamlit as st

CSS_FILE = "style/style.css"

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:" , layout="wide")

col1 , col2 , col3 = st.columns([0.5 ,9 , 0.5])


st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Kontakt/Inicjatywa , skontaktuj się z nami")


message_mail = st.text_input("Twój e-mail")
message_area = st.text_area("Napisz wiadomość")

