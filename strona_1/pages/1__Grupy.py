import streamlit as st
import os


CSS_FILE = "style/style.css"
LOGS = "logs.txt"
ARCHIWUM = "archiwum.txt"
st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:")


with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def f_przenoszenie():
    try:
        with open('logs.txt', 'r') as logs_file:
            logs_content = logs_file.read()

        with open('logs.txt', 'w') as logs_file:
            pass

        with open('archiwum.txt', 'a') as archiwum_file:
            archiwum_file.write(logs_content)
    except:
        print("ERROR")



def f_check(check):
    if check>14:
        f_przenoszenie()



st.title("Aktualna lista")

st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.header("Imię:")
with col2:
    st.header("E-mail:")

def f_write_logs():
    check = 0
    with open(LOGS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Imi"):
                line = line.replace("Imie: ", "")
                with col1:
                    st.write(line)

            elif line.startswith("E-mail"):
                line = line.replace("E-mail: ", "")
                check +=1
                f_check(check)
                with col2:
                    st.write(line)


f_write_logs()


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

                elif line.startswith("E-mail"):
                    line = line.replace("E-mail: ", "")
                    with col2:
                        st.write(line)