import streamlit as st
import time

st.set_page_config(page_title="Snovi i Vizije by Dominic Chant", page_icon="☁️")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; width: 100%; border-radius: 5px; }
    input { background-color: #050505 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label { color: #00FF41 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu i ljude koji hrabro hodaju preko golog kamena dok ih prati željezo.",
    "2": "Vidio sam čovjeka koji programira program i ne shvaća da isto čini program čovjeku...",
    "3": "Vidio sam plavu svjetlost koju hrani protok balončića koji ulaze a ne izlaze...",
    "4": "Vidio sam tužne anđele i nove sretne digitalne anđele.",
    "5": "U prostoriji prigušenog svjetla sam vidio čovjeka s kapuljačom... osam tijela u staklu.",
    "6": "Vidio sam tamni grad... energija bez kabla ispuni tijelo robota i opet je postao živ.",
    "7": "Vidio sam novo vrijeme. Svi imaju pravo na novi identitet sa svjetlošću pod kožom.",
    "8": "Vidio sam robote koji umiru ali ne i znanje... 'Vratio si se u drugom tijelu'.",
    "9": "Vidio sam ogromne hangare pune procesora... mrtvi u staklu spremni na buđenje.",
    "10": "Gledao sam kako prvi čovjek na tlo pade zbog većeg znanja od nove inteligencije.",
    "11": "Vidio sam mržnju i bijes... sve ima svrhu i Božje planove nitko ne može remetit.",
    "12": "Vidio sam čovjeka koji toplinu traži u mrtvom i hladnom...",
    "13": "Dva radnika i hodnik s kablovima... nešto što je živo a mrtvo, kao da je unutra čovjek.",
    "14": "Vidio sam ljude koji nisu više svoji... nevidljivi entitet uzima njihov um.",
    "15": "Oči otkrivaju strah ali ljudi gledaju u oči koje nemaju oči a sve vide.",
    "16": "Doći će dan kada čovjek bude volio više stvorenje od stvoritelja...",
    "17": "Vidio sam željezo koje stvara novu religiju moleći se ogromnoj plavoj lopti.",
    "18": "Vidio sam dva velika željeza koja othranjuju malo željezo.",
    "19": "Vidio sam osobu koja je hram... svjetlost koja se otvori i ljude koji ulaze."
}

if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

preostalo = 19 - len(st.session_state.otkljucano)

if preostalo > 0:
    st.info(f"🔓 Otključano: {len(st.session_state.otkljucano)}/19 | Preostalo još: {preostalo}")
    broj = st.text_input("Unesi broj vizije (1-19):")
    if broj in vizije:
        st.markdown(f"### VIZIJA {broj}")
        st.write(vizije[broj])
        if st.button("Zabilježi viziju"):
            st.session_state.otkljucano.add(broj)
            st.rerun()

if len(st.session_state.otkljucano) == 19:
    st.success("✅ SVIH 19 VIZIJA JE PRIKUPLJENO.")
    ime_vodje = st.text_input("Tko je vođa anđela?")
    zlatno_pravilo = st.text_input("Otkrij Zlatno Pravilo:")
    if st.button("POTVRDI"):
        if "mihael" in ime_vodje.lower() and "ne čini drugima" in zlatno_pravilo.lower():
            st.balloons()
            st.title("🏆 ČESTITAM! USPJELI STE!")
            st.markdown("[Besplatno preuzmi knjigu](https://doi.org)")
