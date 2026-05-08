import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Técnicos",
    page_icon="🧑‍🔧",
    layout="wide",
)

@st.cache_data
def carregar_dados():
    return pd.read_csv("micexemplo.csv")

st.title("🧑‍🔧 Página de Técnicos")


st.write("Acompanhe o volume de manutenções realizadas por cada técnico da equipe e visualize os custos atrelados aos atendimentos.")


st.markdown("---")

df = carregar_dados()


st.sidebar.header("Filtro de Técnicos")
tecnicos_lista = ["Todos"] + sorted(df["Técnico Responsável"].dropna().unique().tolist())
tecnico_selecionado = st.sidebar.selectbox("Escolha o Técnico", tecnicos_lista)

if tecnico_selecionado == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["Técnico Responsável"] == tecnico_selecionado]


st.subheader("Manutenções por Técnico")
df_tabela_tecnicos = df_filtrado[["ID", "Técnico Responsável", "Equipamento", "Custo (R$)"]]
st.dataframe(df_tabela_tecnicos, use_container_width=True)

st.markdown("---")


st.sidebar.header("Gráfico de Atendimentos")
tipo_grafico = st.sidebar.selectbox("Escolha o tipo de gráfico", ["Barra", "Linha"])

st.subheader("Quantidade de Manutenções por Técnico Responsável")

grafico_qtd = df_filtrado.groupby("Técnico Responsável").size().rename("Quantidade")

if tipo_grafico == "Barra":
    st.bar_chart(grafico_qtd)
else:
    st.line_chart(grafico_qtd)

st.markdown("---")


if st.button("Voltar para Home"):
    st.switch_page("Home.py")