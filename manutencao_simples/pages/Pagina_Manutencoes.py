import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Manutencoes",
    page_icon="",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    return pd.read_csv("micexemplo.csv")


st.title("Pagina de Manutencoes")

df = carregar_dados()
coluna_tipo_manutencao = next(
    coluna for coluna in df.columns if coluna.startswith("Tipo de Manuten")
)

st.subheader("Tabela completa")
st.dataframe(df, use_container_width=True)

st.sidebar.header("Exercicio 7 - Filtro")
equipamentos = ["Todos"] + sorted(df["Equipamento"].dropna().unique().tolist())
equipamento_selecionado = st.sidebar.selectbox("Filtrar por Equipamento", equipamentos)

if equipamento_selecionado == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["Equipamento"] == equipamento_selecionado]

st.subheader("Exercicio 7 - Manutencoes filtradas")
st.dataframe(df_filtrado, use_container_width=True)

st.sidebar.header("Exercicio 8 - Grafico")
tipo_grafico = st.sidebar.selectbox("Tipo de grafico", ["Barra", "Linha", "Area"])

st.subheader("Exercicio 8 - Quantidade por tipo de manutencao")
grafico = (
    df_filtrado.groupby(coluna_tipo_manutencao)
    .size()
    .rename("Quantidade")
    .sort_index()
)

if tipo_grafico == "Barra":
    st.bar_chart(grafico)
elif tipo_grafico == "Linha":
    st.line_chart(grafico)
else:
    st.area_chart(grafico)

if st.button("Voltar para Home"):
    st.switch_page("Home.py")
