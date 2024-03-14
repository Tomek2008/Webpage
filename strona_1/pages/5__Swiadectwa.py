import streamlit as st

ARCHIWUM = "archiwum.txt"
CSS_FILE = "style/style.css"

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:" , layout="wide")

col1 , col2 , col3 = st.columns([0.1 ,9.8 , 0.1])


st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#st.text_area("Twoje świadectwo")

st.title("Świadectwa")
st.subheader(
 Pragnę podzielić się swoim świadectwem. Po 1 lub 2 konferencji zniknęły u mnie lęki,
odstawiłam leki i już normalnie bez nich funkcjonuję. Jestem spokojniejsza od tego momentu,
niczego się nie boję, śpię dobrze. Z każdą kolejną konferencją i podczas uwielbienia jestem
bardziej cierpliwa i opanowana, radosna, czuję w sercu pokój. Odczuwam w swoim sercu i umyśle
obecność Jezusa Chrystusa, ważę słowa, przestałam używać wulgarnych słów, nauczyłam się modlić.
Za najdrobniejsze rzeczy dziękuję Bogu i widzę owoce Ducha Świętego, jest we mnie a ja w nim.
Po wylaniu Ducha Świętego jest we mnie duża radość, zauważył to mój mąż. Przestałam się bać, lękać.
Codziennie czytam Słowo Boże choć nie wszystko rozumiem i nie potrafię odnieść Go do siebie. 
Czuję się wolna, tzn. uwolniona z problemów, wszystko przyjmuję dużo spokojniej, mam więcej 
cierpliwości i opanowania, częściej się uśmiecham. Czuję się lekka jak piórko. Chwała Panu ❤️
Patrzę na innych doszukując się w nich pozytywów, walorów, zalet. Próbuję ich rozumieć, 
to wszystko nastąpiło po tym jak każdemu kto mnie zranił przebaczyłam. Poprawiła się również moja 
relacja z tymi ludźmi Chwała Bogu ❤️ Zrodziła się we mnie silna potrzeba poznawania Chrystusa i chęć
do czytania Pisma świętego. Chcę kontynuować swoją relację Panem Bogiem i uczestniczyć w Filarze
Wiary. Dziękuję za Was i Waszą posługę.
Agata)
st.title(        )
st.subheader(
    


