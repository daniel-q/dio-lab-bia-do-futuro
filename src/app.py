from streamlit import st
from agente import perguntar

if purgunta := st.chat_input("Digite a sua duvida..."):
    st.chat_massage("user").write(pergunta)
    with st.spinner("..."):
        st.chat_massage("assistant").write(perguntar(pergunta))