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

with  col2:
st.title("Świadectwo 1")
st.subheader(
    "Pragnę podzielić się swoim świadectwem. Po 1 lub 2 konferencji zniknęły u mnie lęki, odstawiłam leki i już normalnie bez nich funkcjonuję. Jestem spokojniejsza od tego momentu, niczego się nie boję, śpię dobrze. Z każdą kolejną konferencją i podczas uwielbienia jestem bardziej cierpliwa i opanowana, radosna, czuję w sercu pokój. Odczuwam w swoim sercu i umyśle obecność Jezusa Chrystusa, ważę słowa, przestałam używać wulgarnych słów, nauczyłam się modlić. Za najdrobniejsze rzeczy dziękuję Bogu i widzę owoce Ducha Świętego, jest we mnie a ja w nim. Po wylaniu Ducha Świętego jest we mnie duża radość, zauważył to mój mąż. Przestałam się bać, lękać. Codziennie czytam Słowo Boże choć nie wszystko rozumiem i nie potrafię odnieść Go do siebie. Czuję się wolna, tzn. uwolniona z problemów, wszystko przyjmuję dużo spokojniej, mam więcej cierpliwości i opanowania, częściej się uśmiecham. Czuję się lekka jak piórko. Chwała Panu ❤️ Patrzę na innych doszukując się w nich pozytywów, walorów, zalet. Próbuję ich rozumieć, to wszystko nastąpiło po tym jak każdemu kto mnie zranił przebaczyłam. Poprawiła się również moja relacja z tymi ludźmi Chwała Bogu ❤️ Zrodziła się we mnie silna potrzeba poznawania Chrystusa i chęćdo czytania Pisma świętego. Chcę kontynuować swoją relację Panem Bogiem i uczestniczyć w Filarze Wiary. Dziękuję za Was i Waszą posługę. Agata")
st.title("Świadectwo 2")
st.subheader( 
    "Uczestniczyłem w Kursie Fundament, który się właśnie zakończył. W pierwszej konferencji „Słowo” miałeś poznanie że jest chłopak który wychowywał się bez ojca. Mój ojciec był obecny w domu tylko fizycznie ale cale życie nie interesował się mną. Tak naprawdę nie było go w moim życiu. Później dodałeś żeby przyjąć uzdrowienie z oglądania stron które prowadzą do nieczystości i że walczy ten ktoś z tym o własnych siłach i brzydzi się tym grzechem całym sobą ale nie może z tym zerwać. Pierwsza konferencja 1:01:57 zaczynasz o tym mówić. Wiedziałem że to chodzi wtedy o mnie , powiedziałem że przyjmuje uzdrowienie i począłem potężne ciarki na swoim ciele od czubka głowy do stóp. Przez chwilę poczułem jakby jakieś zamroczenie moich oczu i ciała. Od tamtej pory jestem wolny. Nawet nie myślę o tym żeby wejść na jakąś stronę i coś oglądać. Przez Kurs Fundament wiele się zmieniło na lepsze, a punktem kulminacyjnym było uwielbienie w Środę podczas Chrztu w Duchu Świętym. Wtedy Duch Święty wlał Bożą Miłość do mojego serca i czuje się kochany. Wiem że choć mój tata ziemski mnie nie chciał to teraz wiem że to nie szkodzi, wiem do kogo należę i tym Kimś jest sam Bóg. Chwała Panu za wielkie dzieła które Pan Bóg czyni, poznałem Go jako Ojca dobrego I miłosiernego, pełnego miłości. Jestem wolny! Jestem wdzięczny Tobie I całej waszej wspólnocie za Wasza posługę w imieniu Jezusa. Mam nadzieję że się jeszcze kiedyś spotkamy w tej ziemskiej wędrówce. Pozdrawiam. Paweł") 
    


