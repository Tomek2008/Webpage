import streamlit as st
import os

ARCHIWUM = "archiwum.txt"
CSS_FILE = "style/style.css"

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:")

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def f_archiwum():
    st.title("Archiwum")

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Imię")
        st.write("###")
        st.write("###")

    with col2:
        st.header("Data")
        st.write("###")
        st.write("###")


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

                elif line.startswith("E-mail"):
                    line = line.replace("E-mail: ", "")
                    with col2:
                        st.write(line)

f_archiwum()
