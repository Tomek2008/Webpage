import streamlit as st

CSS_FILE = "style/style.css"


st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:" , layout="wide")

col1 , col2 , col3 = st.columns([0.1 ,9 , 0.1])


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

st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Stanowisko kościoła")

st.write("---")

tekst = """

Powyższe modlitwy i towarzyszące im obietnice, zostały przepisane z książeczki, wydrukowanej w Tuluzie w 1740 roku i wydanej przez Ojca Adriana Parvilliersa z Towarzystwa Jezusowego, misjonarza apostolskiego Ziemi Świętej. Z pozwoleniem, aprobatą i poleceniem ich rozpowszechniania. Przetłumaczono je na wiele języków, w tym także na język polski.

Za czasów świętej Brygidy w XIV wieku nie było jeszcze techniki drukarskiej. Dlatego uciekano się do pracowitej usługi kopistów. Papież Urban VI zachęcał ich do zwiększania ilości egzemplarzy opisu objawień świętej Brygidy. O te teksty ubiegali się królowie, władcy, biskupi, uniwersytety, klasztory, biblioteki.

Książki, zawierające powyższe modlitwy i związane z nimi obietnice, uzyskały potwierdzenia wielu dostojników kościelnych, jak jego Eminencji Kardynała Giraud z Cambrai w 1845 roku, Monsignora Floriana arcybiskupa Tuluzy w 1863 roku. Książeczki, zawierające te modlitwy, otrzymały błogosławieństwo Jego Świątobliwości Papieża Piusa IX 31 maja 1862 r.

Ci, którzy zwiedzają bazylikę świętego Pawła w, Rzymie, mogą zobaczyć krucyfiks o wielkości naturalnej, dzieło rzeźbiarza Piotra Cavalliniego, przed którym klęczała św. Brygida. Tutaj przeprowadziła ona swoją cudowną rozmowę z Chrystusem Ukrzyżowanym.

Podstawowy tekst tej religijnej broszurki w tłumaczeniu na pięć języków został przedłożony Kongregacji św. Obrzędów dnia 20 kwietnia 1950 roku. Wydawca: Casa di Padre Pio Case postale 231, Saint-Remi, Que., Canada.

Piętnaście modlitw, objawionych św. Brygidzie zwanych popularnie "Tajemnicą szczęścia", cieszy się od wielu lat żywym zainteresowaniem poszczególnych osób i różnych środowisk modlitewnych. Kościół udzielał im kilkakrotnie swojej aprobaty, jak to wynika z powyższego opisu. Również dla przekładu polskiego władza kościelna wyraziła swoją zgodę.

"""

st.write(tekst)
