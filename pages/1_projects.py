import streamlit as st

st.write("# :red[Projects]")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("IVVQ")
    st.image("assets/uml_acc.jpg")

with col2:
    st.header("Data Analyse")

with col3:
    st.header("Développement Embarqué")