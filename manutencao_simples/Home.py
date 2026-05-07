import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Dashboard de Manutencoes",
    page_icon="",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    return pd.read_csv("micexemplo.csv")


st.title("Dashboard de Manutencoes")
st.write("Bem-vindo ao painel de acompanhamento das manutencoes industriais.")

df = carregar_dados()

st.subheader("Previa dos dados")
st.dataframe(df, use_container_width=True)

st.subheader("Navegacao")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Pagina de Manutencoes", use_container_width=True):
        st.switch_page("pages/Pagina_Manutencoes.py")

with col2:
    if st.button("Pagina de Custos", use_container_width=True):
        st.switch_page("pages/Pagina_Custos.py")

with col3:
    if st.button("Pagina de Tecnicos", use_container_width=True):
        st.switch_page("pages/Pagina_Tecnicos.py")
