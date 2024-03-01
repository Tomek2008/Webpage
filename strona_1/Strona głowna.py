import streamlit as st
import smtplib
from email.mime.text import MIMEText
import datetime
import pandas as pd


LOGS = "logs.txt"

MAIL = {"mail":"kupakubakupa123@outlook.com" , "passwd":"Tomasz123#"}

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:" , layout="wide")

col1 , col2 , col3 = st.columns([0.1 ,9.8 , 0.1])


st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

col1 , col2 , col3 , col4  = st.columns(4)


def f_write_logs():
    with open(LOGS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Imi"):
                line = line.replace("Imie: ", "")
                with col1:
                    st.write(line)

            elif line.startswith("E-mail"):
                line = line.replace("E-mail: ", "")
                with col2:
                    st.write(line)

            elif line.startswith("Stan"):
                line = line.replace("Stan: ", "")
                with col3:
                    st.write(line)

            elif line.startswith("Data"):
                line = line.replace("Data: ", "")
                with col4:
                    st.write(line)

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

def footer():
    st.code("  ŻYWA TAJEMNCIA SZCZĘŚCIA\n"
            "  KONTAKT POD NUMEREM {...}")


def f_write_logs():
    data = {"Imie": [], "Stan": [], "Data": []}

    with open(LOGS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Imie"):
                line = line.replace("Imie: ", "").strip()
                data["Imie"].append(line)
            elif line.startswith("Stan"):
                line = line.replace("Stan: ", "").strip()
                data["Stan"].append(line)
            elif line.startswith("Data"):
                line = line.replace("Data: ", "").strip()
                data["Data"].append(line)

    df = pd.DataFrame(data)
    st.table(df)

col1 , col2  = st.columns([5 , 5])

def send_mail(mail, tytul, tresc):

    email_sender = MAIL["mail"]
    email_receiver = mail
    subject = tytul
    body = tresc
    password = MAIL["passwd"]
    msg = MIMEText(body)
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, msg.as_string())
    server.quit()



def save_user(mail, imie , stan):
    with open(LOGS, 'a') as file:
        file.write(f"E-mail: {mail}\n")
        file.write(f"Imie: {imie}\n")
        file.write(f"Stan: {stan}\n")
        file.write(f"Data: {datetime.datetime.now()}\n")
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

def check_user():
    with open(LOGS , "r") as file:
        line_count = sum(1 for line in file)

    line_count =line_count // 5
    print(line_count)
    if line_count > 15:
        return True

    return False

with col1:



    if 'show' not in st.session_state:
        st.session_state.show = False



    st.title("Módlmy się wspólnie")
    st.subheader(
        "Razem tworzymy piętnastoosobowe grupy, w których każda osoba codziennie rozważa jedną z piętnastu Tajemnic Męki Pańskiej, objawioną św. Brygidzie Szwedzkiej. Modlitewne trwanie przy Jezusie Konającym poprzez przynależność do Żywej Tajemnicy Szczęścia będzie trwać przez cały rok, lub przez dłuższy czas, jeśli ktoś będzie miał taką wolę.")

    form_expanded = st.button("Dołącz do grupy modlitewnej")

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
                        tytul1 = f"Potwierdzenie chęci udziału"
                        tresc1 = (
                            f"Witaj, {imie}. "
                            f"Właśnie zapisałeś się do grupy modlitewnej. Przez następny rok będziesz otrzymywał modlitwy, "
                            f"które będą zmieniać się co tydzień. Jest 15 modlitw, więc każdą modlitwę będziesz odprawiał około 4 razy. ")

                        st.warning(f"Wysyłanie e-maila na {mail}, czekaj")
                        try:
                            send_mail(mail, tytul=tytul1, tresc=tresc1)
                        except Exception as e:
                            st.error("Błąd wysyłania maila")
                        finally:
                            st.success("Wysłano e-maila 🚀")
                            save_user(mail, imie , stan="Niezweryfikowany")
                            st.success(f"Zostałeś zapisany , witaj {imie}")
                            if check_user():
                                try:
                                    with open('logs.txt', 'r') as logs_file:
                                            logs_content = logs_file.read()

                                    with open('logs.txt', 'w') as logs_file:
                                        pass

                                    with open('archiwum.txt', 'a') as archiwum_file:
                                        archiwum_file.write(logs_content)
                                except Exception as e:
                                    print(e)

                    else:
                        st.warning("Ten e-mail jest już zarejestrowany")

                else:
                    st.warning("E-mail musi zawierać @")
            else:
                st.warning("Wprowadz obie wartości")

with  col2:
    st.image("assets/img2.png", use_column_width=True)

st.title("Obietnice Pana Jezusa")
st.subheader(
    "Od dłuższego czasu Brygida pragnęła wiedzieć, ile ciosów Chrystus Pan otrzymał podczas swej Męki. Pewnego dnia Zbawiciel objawił się jej i rzekł")
st.subheader(
    '"Moje Ciało otrzymało 5480 ciosów. Jeżeli chcesz je uczcić pobożną praktyką, zmów 15 Ojcze nasz i 15 Zdrowaś z modlitwami, których cię nauczyłem podczas całego roku w ten sposób w ciągu roku uczcisz każdą Moją Ranę"')
st.header("Potem w formie obietnicy dodał, że ktokolwiek zmówi te modlitwy podczas roku:")
st.subheader("1. Uwolni 15 dusz ze swej rodziny z czyśćca.")
st.subheader("2. 15 sprawiedliwych spośród krewnych zostanie potwierdzonych i zachowanych w łasce.")
st.subheader("3. 15 grzeszników spośród krewnych zostanie nawróconych.")
st.subheader("4. Osoba, która zmówi te modlitwy, osiągnie pewien stopień doskonałości.")
st.subheader(
    "5. Już na 15 dni przed śmiercią będzie przeżywała szczery żal za wszystkie popełnione grzechy z świadomością ich ciężkości.")
st.subheader(
    "6. Na 15 dni przed śmiercią dam jej Moje najświętsze Ciało, ażeby przez Nie została uwolniona od głodu wiecznego oraz dam jej Moją drogocenną Krew do picia, by na wieki nie doznała dokuczliwego pragnienia.")
st.subheader("7. Położę przed nią Mój zwycięski Krzyż jako pomoc i obronę przeciw zasadzkom nieprzyjaciół")
st.subheader("8. Przed jej śmiercią przyjdę do niej z Moją najdroższą i ukochaną Matką")
st.subheader("9. Przyjmę z dobrocią jej duszę i zaprowadzę do wiecznej radości.")
st.subheader(
    "10. Zaprowadziwszy ją tam, dam jej kosztować z przedziwnej studni Mojej Boskości, czego nie uczynię tym, którzy nie odmawiali tych czy podobnych modlitw.")
st.subheader(
    "11. Trzeba wiedzieć, że choćby ktoś żył przez 30 lat w grzechu, lecz potem skruszonym sercem odmawiałby pobożnie te modlitwy albo przynajmniej powziął postanowienie ich odmawiania, Pan mu odpuści jego grzechy.")
st.subheader("12. Obroni go przed zgubnymi pokusami.")
st.subheader("13. Zachowa mu pięć zmysłów.")
st.subheader("14. Uchroni go przed nagłą śmiercią.")
st.subheader("15. Uwolni jego duszę od kar wiecznych")
st.subheader("16. Człowiek ten otrzyma wszystko, o co poprosi Pana Boga i Najświętszą Pannę.")
st.subheader(
    "17. Jeśliby ktoś żył zawsze według woli Boga i musiałby umrzeć przedwcześnie, życie jego zostanie przedłużone.")
st.subheader("18. Ktokolwiek zmówi te modlitwy, uzyska za każdym razem odpust cząstkowy.")
st.subheader("19.Człowiek ten otrzyma zapewnienie, że cieszyć się będzie szczęściem chórów anielskich.")
st.subheader(
    "20. Każdy, kto by innych nauczył tych modlitw, nie będzie nigdy pozbawiony radości i zasługi, ale one trwać będą wiecznie.")
st.subheader("21. Tam, gdzie odmawia się te modlitwy, Bóg jest obecny swoją łaską.")



with open(LOGS , "r") as file:
    linecount = sum(1 for line in file)
    linecount=linecount//5

tekst  = (f"W tym momencie zapisane są {linecount} osoby")
st.title(tekst)

f_write_logs()

if st.button("Zobacz grupy"):
    st.switch_page("pages/1__Grupy.py")

st.write("---")

footer()
