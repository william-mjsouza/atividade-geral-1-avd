import streamlit as st


st.set_page_config(
    page_title="Tecnicos",
    page_icon="",
    layout="wide",
)

st.title("Pagina de Tecnicos")
st.write("Pagina criada para a proxima etapa da atividade.")

if st.button("Voltar para Home"):
    st.switch_page("Home.py")
