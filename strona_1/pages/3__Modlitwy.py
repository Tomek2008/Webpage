import streamlit as st

CSS_FILE = "style/style.css"

st.set_page_config(page_title="Żywa Tajemnica szczęścia", page_icon=":smile:" , layout="wide")

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1 , col2 , col3 = st.columns([0.1 ,9.8 , 0.1])

st.write("---")

with col2:
    st.image("assets/img1.png", use_column_width=True)

st.title("Modlitwy")


switch_state = st.checkbox("Rosyjski")


if switch_state:
    lang = "ros"
else:
    lang = "pol"

if lang == "pol":
    modlitwy_text = """

    PIERWSZA MODLITWA

    O Jezu Chryste! Słodkości odwieczna wszystkich obejmujących Cię miłością. Radości przewyższająca wszelkie szczęście i oczekiwanie, prawdziwe Zbawienie i Nadziejo każdego grzesznika. Ty, który objawiłeś, że największym Twoim zadowoleniem jest być między ludźmi, tak że z miłości dla nich po upływie zapowiedzianych czasów przyjąłeś naturę ludzką, wspomnij sobie, o Jezu, wszystkie cierpienia zniesione od chwili poczęcia, a zwłaszcza w czasie swojej świętej Męki, jak to przewidziała odwieczna myśl Boża i jak zadecydowała wola Najwyższego.
    Wspomnij sobie, Panie, że urządzając Wieczerzę Eucharystyczną wraz z uczniami, po umyciu im nóg, dałeś swoje Najświętsze Ciało i drogocenną Krew, a udzielając pociechy z właściwą sobie dobrocią przepowiedziałeś bliską swoją Mękę. Wspomnij na smutek i gorycz, które w udręczonej Duszy odczułeś, wyznając wobec najbliższego otoczenia: "Smutna jest dusza moja aż do śmierci".

    Wspomnij wszystkie obawy, niepokoje i boleści, które Twoje delikatne Ciało zniosło przed ukrzyżowaniem, kiedy po odprawieniu po raz trzeci modlitwy, oblewając się krwawym Potem, zostałeś zdradzony przez swojego ucznia Judasza, aresztowany przez wybrany naród, oskarżony przez fałszywych świadków, niesprawiedliwie sądzony przez trzech sędziów tuż przed uroczystym świętem Wielkanocy czyli Paschy. Wspomnij, że przywiązano Cię do słupa i rozdarto Ciało biczami, że byłeś obnażony z własnych szat i odziany w inny strój na pośmiewisko, że Cię ukoronowano cierniami do ręki włożono trzcinę, zasłonięto oczy i twarz, że Cię policzkowano i obrzucono obelgami.

    Na pamiątkę tych wszystkich zniewag i boleści, które wycierpiałeś w okresie poprzedzającym Mękę Krzyża, daj mi przed nadejściem śmierci przeżyć prawdziwą skruchę serca, szczerą i całkowitą spowiedź, odprawić godne zadośćuczynienie i otrzymać odpuszczenie wszystkich grzechów. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    DRUGA MODLITWA

    O Jezu! Prawdziwa wolności Aniołów, Raju niezmąconego szczęścia, wspomnij sobie na odrazę i smutek, które odczułeś, kiedy nieprzyjaciele otoczyli Cię jak wściekłe lwy i tysiącami zniewag, policzkowaniem, kaleczeniem i innymi wymyślnymi udrękami prześcigali się w zadawaniu cierpień. Ze względu na te tortury i stek obelżywości, błagam Cię, Boski Zbawicielu, wyzwól mnie z więzów wszystkich nieprzyjaciół widzialnych i niewidzialnych, a roztaczając błogosławioną opiekę prowadź drogą doskonałości do zbawienia wiecznego. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    TRZECIA MODLITWA

    O Jezu! Stworzycielu nieba i ziemi, którego żadna rzecz nie może ograniczyć ani objąć, Ty który ogarniasz i zespalasz wszystko swoją potęgą, wspomnij sobie na gorzką boleść, którą odczuwałeś, kiedy kaci, przywiązując Twoje święte Ręce i Nogi do krzyża, przeszyli je na wylot grubymi, stępionymi gwoździami. Rozciągając Cię z niesłychanym okrucieństwem na krzyżu, nie syci Twych cierpień, miotali obelgi na wszystkie strony i dając upust swojej wściekłości, powiększali Twoje Rany przez zadawanie dodatkowych katuszy.
    Ze względu na ogrom cierpień, których doświadczyłeś podczas ukrzyżowania, daj mi Twoją świętą bojaźń i Twoją prawdziwą miłość. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    CZWARTA MODLITWA

    O Jezu! Lekarzu niebieski, wzniesiony na krzyżu, by nasze rany uleczyć Twoimi, wspomnij na obicia i złamania, jakich doznałeś w swoich członkach, tak, że każdy z nich został w jakiś sposób naruszony. Od stóp do głowy nie znaleziono miejsca na Twoim Ciele, które nie byłoby pokryte raną. W takim stanie poniżenia, zapominając o własnych cierpieniach, nie przestawałeś modlić się do Ojca za nieprzyjaciół słowami: "Ojcze odpuść im, bo nie wiedzą co czynią"!
    Na mocy tego bezgranicznego Miłosierdzia i na pamiątkę owej boleści, spraw, żeby pamięć o Twojej gorzkiej Męce przywiodła nas do doskonałej skruchy i przyniosła odpuszczenie wszystkich popełnionych grzechów. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    PIĄTA MODLITWA

    O Jezu! Zwierciadło odwiecznego Blasku, wspomnij na smutek, którego doznałeś, kiedy w świetle Boskiego poznania, rozważając nad przeznaczeniem tych, którzy mieli być odkupieni dzięki zasługom Twojej świętej Męki, widziałeś zarazem wielkie tłumy skazanych, którzy szli na potępienie z powodu rozlicznych grzechów. Żal Ci było tych nieszczęśliwych ludzi zgubionych i zrozpaczonych.
    Przez to bezgraniczne współczucie i miłosierdzie, a zwłaszcza przez wzruszającą dobroć okazaną skruszonemu łotrowi współukrzyżowanemu na Golgocie, kiedy mu powiedziałeś: "Dziś ze Mną będziesz w raju!", błagam Cię o słodki Jezu, okaż miłosierdzie mnie grzesznemu w godzinę śmierci. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    SZÓSTA MODLITWA

    O Jezu! Łaskawy i upragniony Królu, wspomnij na boleść, którą odczułeś, kiedy nagi jak nędzarz, przykuty do krzyża, zostałeś na tym drzewie hańby wyśmiany i wzgardzony. Wszyscy Twoi krewni i przyjaciele opuścili Cię z wyjątkiem ukochanej Matki, która stała wiernie przy Tobie podczas konania. Ty zaś poleciłeś Ją swojemu wiernemu Uczniowi, mówiąc do Najświętszej Maryi Panny: "Niewiasto, oto syn Twój" i do świętego Jana: "Oto Matka Twoja!"
    Błagam Cię, o mój Zbawicielu, przez miecz boleści, który ongiś przeszył duszę Twojej Najboleśniejszej Matki, współczuj ze mną we wszystkich utrapieniach i doświadczeniach, zarówno cielesnych jak i duchowych, abym je wszystkie przezwyciężył w życiu a zwłaszcza w ostatniej godzinie przed nadejściem śmierci. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    SIÓDMA MODLITWA

    O Jezu! Źródło niewyczerpanej litości, który z głęboką miłością wypowiedziałeś na krzyżu tęsknotę: "Pragnę!". Było to pragnienie zbawienia rodzaju ludzkiego. Proszę Cię, o mój Odkupicielu, rozpal pragnienia naszych serc, byśmy wytrwale we wszystkich podejmowanych czynnościach dążyli do doskonałości. Wygaś w nas całkowicie pożądliwość ciała i żądze światowe. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    ÓSMA MODLITWA

    O Jezu! Słodyczy serc, niepojęta Dobroci, przez gorzką żółć i ocet, których skosztowałeś na krzyżu z miłości ku nam, spraw, byśmy godnie przyjmowali Twoje Ciało i Twoją bezcenną Krew, lekarstwo i pociechę naszych dusz, w czasie ziemskiego pielgrzymowania i w godzinie śmierci. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    DZIEWIĄTA MODLITWA

    O Jezu! Cnoto królewska, Radości ducha, wspomnij na boleść, którą znosiłeś, kiedy zatopiony w smutku z powodu zbliżającej się śmierci, znieważony i wykpiony przez Wybrany Naród, opuszczony przez Ojca Twego, wołałeś głośno: "Boże Mój, Boże Mój, czemuś Mnie opuścił?"
    Zaklinam Cię, o mój Zbawicielu, przez doznaną trwogę, abyś mnie nie opuścił podczas cierpienia i trwogi, jakie wywołuje zbliżająca się śmierć i sąd Boży. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    DZIESIĄTA MODLITWA

    O Jezu! Który jesteś Początkiem i Końcem wszystkich rzeczy, Życiem i Szczytem cnót, wspomnij sobie, że ze względu na mnie zostałeś pogrążony w niezmierzonych boleściach. Przez ten bezmiar cierpień, spowodowany okrutnymi Ranami, które zadały grzechy świata, naucz mnie zachowywać z prawdziwą miłością Twoje przykazania, bo one dla tych, którzy Cię kochają są łatwą i jedyną drogą do zbawienia. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    JEDENASTA MODLITWA

    O Jezu! Niezgłębione źródło Miłosierdzia, błagam Cię z uwagi na pamięć o Twoich Ranach, których dojmujący ból doszedł do szpiku kości i wypełnił wszystkie wnętrzności, wyrwij mnie nędznego z grzechu i ukryj mnie w głębi tych Ran przed zagniewanym Obliczem Sprawiedliwości, aż minie Twe oburzenie i słuszny gniew. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    DWUNASTA MODLITWA

    O Jezu! Zwierciadło prawdy, Miłości zwieńczająca wszystkie siły ducha, Znaku jedności, rozdarty i umęczony obfitym upływem godnej uwielbienia Krwi, wspomnij na niezliczone Rany, które okryły Cię od stóp do głowy. O niezmierna i totalna boleści, którą zniosłeś w swym dziewiczym Ciele z miłości ku nam. Jezu Chryste, co mogłeś nadto dla mnie uczynić? Czego jeszcze nie dokonałeś?
    Zaklinam Cię, o mój Zbawicielu, wszystkie swoje Rany znacz drogocenną Krwią w moim sercu, abym mógł w nim ustawicznie czytać boleść i miłość Twoją. Spraw, aby przez moje przylgnięcie do Twojej Męki zaznaczył się w mojej duszy owoc Twych cierpień. Niech Twoja miłość wzrasta w niej codziennie do czasu, aż stanę przed Tobą, Skarbie wszystkich dóbr i wszystkich radości! O słodki Jezu, daj mi w życiu wiecznym, to o co Cię błagam. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    TRZYNASTA MODLITWA

    O Jezu! Odwieczna Potęgo, Królu nieśmiertelny i niezwyciężony, wspomnij na boleść, którą znosiłeś, kiedy opuściły Cię wszystkie siły, zarówno ciała jak i ducha, kiedy skłaniając głowę oświadczyłeś: "Wykonało się". Błagam Cię, Panie Jezu, przez zupełne wyczerpanie i przygniatający niepokój, jakich doznałeś przed dopełnieniem dzieła Odkupienia, zmiłuj się nade mną w ostatniej godzinie życia, kiedy dusza moja będzie w udręce, a serce pełne trwogi. W Tobie ufność pokładam. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    CZTERNASTA MODLITWA

    O Jezu! Jedyny Synu Ojca, Blasku i Wyrazie Jego istoty, wspomnij na serdeczne i pokorne polecenie się Ojcu w ufnej wypowiedzi: "Ojcze, w ręce Twoje oddaję ducha mego". I wtedy skonałeś. Ale choć całe Ciało okaleczałe i zbroczone Krwią, oddając ostatnie tchnienie, przestało żyć Twa Boska moc otworzyła źródło Miłosierdzia i wylała zdroje łask odkupieńczych dla ludzkości.
    Przez tę drogocenną śmierć i wszystkie jej okoliczności błagam Cię, Królu Świętych, wzmocnij mnie i dopomóż w walce przeciw szatanowi, ciału i krwi, ażebym umarły dla świata żył tylko Tobą i dla Ciebie. Proszę gorąco, przyjmij w godzinę śmierci moją pielgrzymią i wygnańczą duszę u bram wieczności. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!

    PIĘTNASTA MODLITWA

    O Jezu! usymbolizowany w życiodajnej winorośli, wspomnij na obficie broczącą Krew, która popłynęła hojnie z Twego Ciała jak wino z dojrzałych gron w tłoczni.
    Przebity włócznią żołnierza, wylałeś wszystką Krew i Wodę do ostatniej kropli. Wisząc wysoko na krzyżu z opadłą Najświętszą Głową, stałeś się jak pęk zeschniętej mirry, bezwładny, odrętwiały, bez śladu życia na zewnątrz i we wnętrzu Ciała, aż do szpiku kości.

    Przez gorzką Mękę i przez wylaną drogocenną Krew błagam Cię, o słodki Jezu, zrań moje serce łaską, ażeby łzy pokuty i miłości stały się dla mnie dniem i nocą tak potrzebne, jak chleb powszedni. Nawróć mnie całkowicie do siebie, aby me serce utworzyło dla Ciebie stałe mieszkanie, aby moja mowa była Ci miła, a koniec życia uwieńczony nadzieją spotkania się z Tobą w raju, gdzie mógłbym Cię chwalić i błogosławić na wieki wraz ze wszystkimi Świętymi. Amen.

    Ojcze nasz, któryś jest w niebie, święć się Imię Twoje; przyjdź Królestwo Twoje, bądź wola Twoja jako w niebie tak i na ziemi. Chleba naszego powszedniego daj nam dzisiaj i odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom i nie wódź nas na pokuszenie, ale nas zbaw ode złego. Amen.

    Zdrowaś Maryjo, łaski pełna, Pan z Tobą, błogosławionaś Ty między niewiastami i błogosławiony owoc żywota Twojego, Jezus. Święta Maryjo, Matko Boża, módl się za nami grzesznymi teraz i w godzinę śmierci naszej. Amen.

    Westchnienie, Jezu, Miłości moja bądź uwielbiony i zmiłuj się nade mną!


    """

if lang == "ros":
    modlitwy_text = """

Первая молитва

Иисусе Христе, вечная услада всех любящих Тебя, высшая Радость и Чаяние, истинное Спасение и Надежда всех грешников. Господи, Ты бесконечно любящий нас и желающий спасения всем людям, в полноту времён принял человеческую природу. Вспомни, Иисусе, всё, что претерпел Ты во все дни земной жизни Своей и, особым образом во время святых Страстей Твоих по предопределению и воле Всевышнего.
Вспомни, Владыка, как на Тайной Вечере, омыв ноги ученикам, дал Ты им Пречистое Тело Своё и драгоценную Кровь. Даруя утешение в безмерной Своей доброте, Ты предсказал близкую гибель Свою.
Вспомни, Господи, тоску и ужас, испытанные Тобою в смятении душевном, Твои слова, обращённые к избранным: «Душа Моя скорбит смертельно». Вспомни все страдания, тревогу и боль, пережитые до Распятия в Гефсиманском саду, как предан Ты был учеником Своим Иудою, как наложили на Тебя руки по ложному свидетельству, как неправедно осудили тебя три судии накануне Пасхи.
Вспомни, как бичевали Тебя, как обнажили и облекли, насмехаясь, в багряницу, как возложили терновый венец и дали в руки трость, как закрывали Тебе глаза и били по щекам, как насмехались и плевали.
Ради памяти тех унижений и страданий, что принял Ты прежде муки Крестной, да святится Имя Твоё! Даруй мне, Милосердный Господи, перед смертью прийти к истинному смирению и с искренним раскаянием получить прощение грехов. Аминь.
Отче наш… Радуйся, Мария…Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Вторая молитва

Иисусе Христе, истинная Слава ангелов, вечная Радость Рая! Вспомни унижения Свои и печаль, когда люди, которых пришёл Ты спасти, окружили Тебя, будто дикие львы, и, глумясь, наносили удары, заставляя страдать от боли.
Ради этих пыток и унижений молю Тебя, Божественный Спаситель наш, избавь меня от козней вражеских, видимых и невидимых, и умножая Твоё благословенное попечение, веди путём духовного возрастания к вечному спасению. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Третья молитва

Иисусе, Творец Вселенной, Ты, непостижимый, нисходишь к нашей слабости и соединяешь её со Своим могуществом. Вспомни те горькие страдания, когда палачи притянули Твои святые руки и ноги к древу Крестному и пробили их насквозь тупыми ржавыми гвоздями, когда, распиная Тебя на Кресте, пылая от злобы, умножали страдания Твои руганью и глумлением, растравляли раны Твои новыми пытками.
Ради безмерного страдания, что перенёс Ты во время Распятия, даруй мне святой страх Твой и истинную любовь. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Четвёртая молитва

Иисусе, Лекарь Небесный, Ты вознёсся на Крест, дабы ранами Своими исцелить наши душевные язвы! Вспомни об избитых и истерзанных членах Твоих, ибо каждый из них пострадал, и нет неизраненного места на Теле Твоём. Но и в этом уничижении, забывая про страдания Свои, Ты непрестанно молился Отцу Небесному за Своих врагов: «Отче, прости им, ибо не ведают, что делают».
Ради безграничного Милосердия Твоего и памяти Твоих горьких мучений, приведи нас к совершенному смирению и даруй прощение всех тяжких грехов наших. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Пятая молитва

Иисусе, Свет предвечный, вспомни печаль Свою, с которою Ты, всё ведающий и проницающий, думал об уделах тех, кого бы могли искупить Твои святые Страдания. Ты видел бесконечные толпы осужденных, по собственным грехам, на вечные муки, и Ты сжалился над несчастными и обречёнными.
Ради Твоего безмерного сострадания и Милосердия, ради великой милости, оказанной раскаявшемуся разбойнику, распятому рядом с Тобою, когда возгласил Ты: «Ныне же будешь со Мною в Раю», умоляю Тебя, Сладчайший Иисусе, окажи и мне Милосердие в час смерти моей. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Шестая молитва

Иисусе, Премилостивый и Пресвятой Владыка мира! Вспомни мучения Свои, когда пригвоздили Тебя ко Кресту, нагого, презираемого и осмеянного. Все друзья и ближние оставили Тебя, кроме Возлюбленной Матери Твоей. Она верно стояла у Креста до последнего воздыхания Твоего. Ты вверил Марию возлюбленному ученику Своему, сказав Пречистой: «Жено, се сын Твой», а святому апостолу Иоанну: «Се, Матерь Твоя».
Умоляю Тебя, избавитель мой, мечом боли, пронзившим наискорбейшую душу Богородицы, пребудь со мною во всех скорбях и испытаниях, телесных и душевных, особым образом, в мой последний, предсмертный час, дабы стойко претерпел я всё и встретил Тебя в вечности. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Седьмая молитва
Иисусе, Благий Господи, Источник неиссякаемого Милосердия! С великой любовью и скорбью возгласил Ты на Кресте: «Жажду», ибо жаждал помиловать род человеческий.
Прошу Тебя, Искупитель наш, воспламени стремления сердца моего к ревности и стойкости в поиске благочестия и совершенства. Угаси во мне пламень страстей и похотей телесных, жажду мирских удовольствий и славы. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Восьмая молитва

Иисусе, Доброта непостижимая, Сладость сердечная! Ради горечи желчи и уксуса, принятых Тобою при Кресте из любви к человекам, соделай нас достойными принимать Твои Тело и Пресвятую Кровь, лекарство и утешение душ наших в земных странствиях и в час смерти нашей. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Девятая молитва

Иисусе, Чистота непостижимая, Радость духовная! Вспомни страдания и угнетение Твоё, тоску перед лицом близящейся смерти. Унижаемый и осмеянный «избранным народом», оставленный Отцом Твоим Небесным, Ты возопил: «Боже Мой! Боже Мой! Для чего Ты Меня оставил?».
Умоляю Тебя, Спаситель мой, ради смертной тоски, Тобою испытанной, не оставляй меня в часы испытаний и тревог, предвестников смерти и Суда Божия. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Десятая молитва

Иисусе, Ты начало и конец всего сущего, Жизни податель и Спасение душ! Вспомни, что по Милосердию Твоему, по снисхождению ко мне, недостойному, претерпел Ты безмерные страдания.
Ради безмерных страданий Твоих от тяжких ран, принятых Тобою за грехи мира, даруй мне до конца дней моих любить Тебя всею душою и хранить Твои заповеди, ибо в соблюдении их единственный путь ко спасению для всех возлюбивших Тебя. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Одиннадцатая молитва

Иисусе, неистощимый Источник Милосердия! Умоляю Тебя ради ран Твоих, боль от которых проницала всю плоть и кости Твои, избавь меня, окаянного, от грехов и укрой во глубине этих ран от праведного гнева Божия, доколе не престанет Твой гнев святой. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Двенадцатая молитва

Иисусе, Зерцало истины, Любовь соединяющая, Средоточие духовных сил! Изнемогший от потери драгоценной Крови Твоей, вспомни о бессчётных ранах, покрывших всё тело Твоё, от головы до пят. Безмерную, всепроницающую боль терпишь Ты из любви к человекам. Что ещё мог бы Ты сделать для меня, чего не сделал!?
Умоляю Тебя, Спаситель мой, запечатлей Своей драгоценной Кровью Твои раны в сердце моём, дабы мне непрестанно чувствовать Твою боль и Твою любовь. Соделай, дабы переживание Твоих Страстей взрастило в душе моей добрый плод Твоих страданий. Да возрастает и умножается во мне Твоя любовь до часа, когда предстану пред Тобою.
Сокровище добра и радости, сладчайший Иисусе! Даруй мне в вечной жизни то, о чём с надеждой умоляю Тебя. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Тринадцатая молитва

Иисусе, предвечное Могущество, Царь бессмертный и непобедимый! Вспомни страдания Тобою пережитые, когда оставили Тебя все силы, телесные и душевные, и, склонив главу, Ты вымолвил: «Свершилось».
Умоляю Тебя, Владыка, безмерным истощением и угнетением Твоим, испытанным Тобою пред свершением Искупления, умилосердись надо мною в последний час жизни моей, когда заколеблется и задрожит в страхе смертном душа моя, и сердце моё исполнится ужасом. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Четырнадцатая молитва

Иисусе, Единородный Сын Отца, Божественный Свет! Вспомни смиренную жертву Твою, за людей Отцу принесённую. Тело Твоё было иссечено и окровавлено, Ты был оплёван, хулим и покинут. Но с последним дыханием возгласил Ты с верою: «Отче, в руки Твои предаю дух Мой». Твоя Божественная смерть обратилась Источником Милосердия, и хлынули потоки благодати, исцеляющей души.
Умоляю Тебя, Царь святых и Господь господствующих, укрепи меня и помоги мне в борьбе с дьяволом. Войди в плоть и в душу мою, чтобы я умер для мира и жил только Тобой и для Тебя. Горячо и неустанно прошу Тебя, доброй смертью заверши моё земное странствие и открой истомившейся душе моей врата в Твой вечный покой. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

Пятнадцатая молитва

Иисусе, райская Виноградная Лоза, дарующая жизнь вечную! Вспомни Кровь, истекавшую из Плоти Твоей, подобно соку из спелых плодов в точиле. Из Твоего ребра, пробитого копием воина, истекли вся Кровь и вода до последней капли. Вознесённый на Кресте, с поникшею головою, Ты застыл, напряжённый в последней муке, израненный и неживой.
Ради горьких страданий Твоих, ради пролитой на Кресте Драгоценной Крови, умоляю тебя, сладчайший Иисусе, рань и моё окаменелое сердце Своей благодатью! Пусть слёзы покаяния и любви станут мне хлебом насущным во все дни и ночи жизни моей. Обрати меня к Себе всецело и сотвори в сердце моём обитель Твою. Да будут угодны Тебе слова молений моих, да будет увенчан конец жизни моей надеждой встречи с Тобою в раю, где я стану славить и благословлять Тебя в сонме святых во веки веков. Аминь.
Отче наш… Радуйся, Мария… Иисусе Премилосердный, будь прославлен и смилуйся надо мною.

    """

st.markdown(modlitwy_text)