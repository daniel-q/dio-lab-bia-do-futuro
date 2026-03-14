import streamlit as st
from agenteT import perguntar

if pergunta := st.chat_input("Digite a sua duvida..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))