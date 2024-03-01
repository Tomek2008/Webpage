import datetime

import streamlit as st
import os

CSS_FILE = "style/style.css"
LOGS = "logs.txt"
ARCHIWUM = "archiwum.txt"
st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:", layout='wide')

col1, col2, col3 = st.columns([0.1, 9.8, 0.1])

st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Archiwum")

st.write("---")
col1, col2, col3, col4 = st.columns(4)


def reduce_top_whitespace():
    # Reducing whitespace on the top of the page
    st.markdown("""
    <style>
    .block-container
    {
        padding-top: 2rem;
        padding-bottom: 0rem;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)


reduce_top_whitespace()


def f_archiwum():
    col1, col2 = st.columns(2)
    with open(ARCHIWUM, 'r') as file1:
        lines = file1.readlines()
        file1.seek(0, os.SEEK_END)
        if not file1.tell():
            file1.seek(0)
            st.write("Plik jest pusty")
        else:
            for line in lines:
                if line.startswith("Imi"):
                    line = line.replace("Imie: ", "")
                    with col1:
                        st.write(line)

                if line.startswith("Imi"):
                    line = line.replace("Data: ", "")
                    with col2:
                        st.write(line)




# Use f_archiwum function to display archive data
f_archiwum()
# Uncomment the line below if you want to display logs data
#f_write_logs()
