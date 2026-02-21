import streamlit as st

st.set_page_config(page_title="Snovi i Vizije by Dominic Chant", page_icon="☁️")

st.markdown("<style>.stApp { background-color: #000000; color: #00FF41; }</style>", unsafe_allow_html=True)
st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu...",
    "19": "Vidio sam osobu koja je hram... svjetlost koja se otvori."
}

broj = st.text_input("Unesi broj vizije (1-19):")
if broj in vizije:
    st.write(vizije[broj])
    if st.button("Zabilježi"):
        st.session_state.otkljucano.add(broj)
        st.rerun()

st.info(f"Otključano: {len(st.session_state.otkljucano)}/19")
