import streamlit as st
import smtplib
from email.mime.text import MIMEText
import random


LOGS = "logs.txt"

MAIL = {"mail":"kupakubakupa123@outlook.com" , "passwd":"Tomasz123#"}

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:")

st.title("Witaj")

st.write("---")

def send_mail(mail, tytul, tresc):

    email_sender = MAIL["mail"]
    email_receiver = mail
    subject = tytul
    body = tresc
    password = MAIL["passwd"]

    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.outlook.com', 587)  # Use 'smtp.outlook.com' for Outlook and 'smtp.outlook.com' for gmail
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        return e


def zapisz_sie(mail, imie):
    with open(LOGS, 'a') as file:
        file.write(f"E-mail: {mail}\n")
        file.write(f"Imie: {imie}\n")
        file.write("---\n")

def get_used_emails():
    used_emails = []
    with open(LOGS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("E-mail:"):
                email = line.split(" ")[1].strip()
                used_emails.append(email)
    return used_emails

def check_email_duplicate(mail):
    return mail in get_used_emails()

def check_maska_wprowadzania(mail):
    if "@" in str(mail):
        return True
    else:
        return False

def generatecode():
    code = random.randint(10000 , 99999)
    return code

def verifycode(x , y):
    print("AA")
    if x==y:
        print("Pomyślna weryfikacja")
        return True
    else:
        print("Niepomyślna weryfikacja")
        return False

if 'show' not in st.session_state:
    st.session_state.show = False

form_expanded = st.button("Chce się zapisać !")

if form_expanded:
    st.session_state.show = not st.session_state.show

show_verify = False

if st.session_state.show:
    mail = st.text_input("E-mail:")
    imie = st.text_input("Imie:")

    if st.button("Zapisz się!"):
        if imie and mail:
            if check_maska_wprowadzania(mail):
                if not check_email_duplicate(mail):
                    save_code = generatecode()
                    tytul1 = f"Potwierdzenie chęci udziału"
                    tresc1 = (
                        f"Witaj, {imie}. "
                        f"Właśnie zapisałeś się do grupy modlitewnej. Przez następny rok będziesz otrzymywał modlitwy, "
                        f"które będą zmieniać się co tydzień. Jest 15 modlitw, więc każdą modlitwę będziesz odprawiał około 4 razy. "
                        f"Wpisz ten kod weryfikacyjny do programu, aby potwierdzić chęci wpisania na stronę ten kod: {save_code}"
                    )
                    st.warning(f"Wysyłanie e-maila na {mail}, czekaj")
                    if send_mail(mail, tytul=tytul1, tresc=tresc1):
                        st.success("Wysłano e-maila")
                        show_verify = True
                    else:
                        st.warning("Błąd wysyłania e-maila")
                else:
                    st.warning("Ten e-mail jest już zarejestrowany")

            else:
                st.warning("E-mail musi zawierać @")
        else:
            st.warning("Wprowadz obie wartości")

if show_verify:
    st.write(save_code)
    user_code = st.text_input("Zweryfikuj kod")

    with st.form("verification_form"):
        verify_button_clicked = st.form_submit_button("Zweryfikuj kod")

        print(f"Button Clicked: {verify_button_clicked}")  # Add this line for debugging
        print(f"user_code: {user_code}")  # Add this line for debugging

        if verify_button_clicked and user_code:  # Ensure user_code is not empty
            print("Button clicked!")  # Add this line for debugging
            print("HERE")  # Add this line for debugging

            verifycode(save_code, int(user_code))

