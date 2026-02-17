import streamlit as st
import pandas as pd
from Utilidades import leitura_dados
import requests
import base64

@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()

leitura_dados()

anos = list(range(17, 24))
ano_selecionado = st.sidebar.selectbox('Ano do Fifa',
                               anos,
                               index = len(anos) - 1)

df_data = st.session_state['dados'][f'df_fifa{ano_selecionado}']
df_data = df_data[df_data['Contract Valid Until'] >= ano_selecionado]

clubes = df_data['Club'].unique()
clube_selecionado = st.sidebar.selectbox('Clube:',
                     list(clubes))

jogadores = df_data.loc[df_data['Club'] == clube_selecionado, 'Name']
jogador_selecionado = st.sidebar.selectbox('Jogador: ',
                     jogadores.to_list())

jogador_stats = df_data[df_data['Name'] == jogador_selecionado].iloc[0]

st.image(load_image_64(jogador_stats['Photo']))
st.title(jogador_stats['Name'])
st.markdown(f'**Clube:** {jogador_stats['Club']}')

st.markdown(f'**Posição:** {jogador_stats["Position"]}')

col1, col2, col3 = st.columns(3)

col1.markdown(f'**Idade:** {jogador_stats['Age']}')
col2.markdown(f'**Altura:** {jogador_stats['Height']}')
col3.markdown(f'**Peso:** {jogador_stats['Weight']}')
st.divider()

st.subheader(f'Overall: {jogador_stats['Overall']}')
st.progress(int(jogador_stats['Overall']))
st.divider()

col21, col22, col23 = st.columns(3)

col21.metric('Valor de mercado', value = f' {jogador_stats['Value']}')
col22.metric('Renumeração semanal', value = f' {jogador_stats['Wage']}')
if ano_selecionado >= 22:
    col23.metric('Cláusula de Recisão', value = f' {jogador_stats['Release Clause']}')
else:
    col23.metric('Contratto válido até', value = f' {int(jogador_stats['Contract Valid Until'])}')    