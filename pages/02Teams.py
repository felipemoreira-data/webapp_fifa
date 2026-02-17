import streamlit as st
import pandas as pd
import requests
import base64
from Utilidades import leitura_dados


@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()

def preprocess_row(url):
    if isinstance(url, str) and url.startswith("http"):
        return load_image_64(url)
    return url

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

df_filtrado = df_data[(df_data['Club'] == clube_selecionado)].set_index('Name')
df_filtrado["Club Logo"] = df_filtrado["Club Logo"].apply(preprocess_row)
st.image(df_filtrado.iloc[0]['Club Logo'])
st.markdown(f'## {clube_selecionado}')

columns = ['Age', 'Photo', 'Flag', 'Overall', 'Value', 'Wage', 'Joined', 'Height', 'Weight', 'Contract Valid Until']
df_filtrado = df_filtrado[columns]

df_filtrado["Photo"] = df_filtrado["Photo"].apply(preprocess_row)
df_filtrado["Flag"] = df_filtrado["Flag"].apply(preprocess_row)

def convert_wage(value):
    value = value.replace('€', '')
    
    if 'K' in value:
        return float(value.replace('K', '')) * 1000
    if 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    
    return float(value)

df_filtrado['Wage'] = df_filtrado['Wage'].apply(convert_wage)


st.dataframe(df_filtrado,
              column_config = {
                  'Overall' : st.column_config.ProgressColumn(
                      'Overall', format = '%d', min_value = 0, max_value = 100),
                  'Wage' : st.column_config.ProgressColumn('Weekly Wage', format = '€%f', min_value = 0, max_value = df_filtrado['Wage'].max()),
                  'Photo' : st.column_config.ImageColumn(),
                  'Flag' : st.column_config.ImageColumn('Country')
                
              })
