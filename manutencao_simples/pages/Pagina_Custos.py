import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Custos",
    page_icon="💰",
    layout="wide",
)

@st.cache_data
def carregar_dados():
    return pd.read_csv("micexemplo.csv")

st.title("Página de Custos")

st.write("Nesta página, você pode analisar os custos associados a cada equipamento e filtrar as manutenções pelo seu status atual.")

st.markdown("---")

df = carregar_dados()

st.sidebar.header("Filtro de Custos")
status_lista = ["Todos"] + sorted(df["Status"].dropna().unique().tolist())
status_selecionado = st.sidebar.selectbox("Filtrar por Status", status_lista)

if status_selecionado == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["Status"] == status_selecionado]

st.subheader("Tabela de Custos")
df_tabela_custos = df_filtrado[["ID", "Equipamento", "Custo (R$)", "Status"]]
st.dataframe(df_tabela_custos, use_container_width=True)

st.markdown("---")


st.sidebar.header("Gráfico de Custos")
tipo_grafico = st.sidebar.selectbox("Escolha o tipo de gráfico", ["Barra", "Linha", "Área"])

st.subheader("Custo Total por Equipamento")

grafico_custo = df_filtrado.groupby("Equipamento")["Custo (R$)"].sum()

if tipo_grafico == "Barra":
    st.bar_chart(grafico_custo)
elif tipo_grafico == "Linha":
    st.line_chart(grafico_custo)
else:
    st.area_chart(grafico_custo)

st.markdown("---")


if st.button("Voltar para Home"):
    st.switch_page("Home.py")