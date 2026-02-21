import streamlit as st

st.set_page_config(page_title="Snovi i Vizije", page_icon="☁️")

st.markdown("<style>.stApp { background-color: #000; color: #00FF41; }</style>", unsafe_allow_html=True)

st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

st.write("---")
st.info("Sustav je online. Unesite broj vizije ispod.")

broj = st.text_input("Broj (1-19):")
if broj == "1":
    st.success("Vizija 1: U snu sam vidio strašno vrijeme...")
elif broj == "19":
    st.success("Vizija 19: Vidio sam osobu koja je hram...")

st.write("---")
st.write("Ako vidite ovaj tekst, aplikacija RADI.")
