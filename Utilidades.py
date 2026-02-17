from pathlib import Path
import streamlit as st
import pandas as pd

def tratar_dataframe (df):
    df = df.replace(r'<.*?>', '', regex=True)
    df['Contract Valid Until'] = pd.to_numeric(df['Contract Valid Until'], errors= 'coerce')
    #df = df[df['Contract Valid Until'] >= 2023]
    if 'Club Logo' in df.columns:
        df['Club Logo'] = df['Club Logo'].str.replace('light_30.png', '30.png', regex=False)
    df = df[df['Value'].str.replace('€', '', regex= False).str.replace('M', '', regex= False).str.replace('K', '', regex= False).astype(float) > 0]
    df = df.sort_values(by = 'Overall', ascending= False)
    return df
def massa_altura(df):
    altura = df['Height'].str.extract(r"(\d+)'(\d+)").astype(float)
    df['Height'] = ((altura[0] * 12 + altura[1]) * 2.54).round(0).astype(int).astype(str) + 'cm'

    df['Weight'] = (df['Weight'].str.replace('lbs', '', regex=False).astype(float).mul(0.45359237).round(0).astype(int).astype(str) + 'kg')
    return df

def leitura_dados():
    if  'data' not in st.session_state:
        pasta_datasets = Path(__file__).parent / 'dataset'
        df_fifa17 = pd.read_csv(pasta_datasets / 'FIFA17_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa17 = tratar_dataframe(df_fifa17)
        df_fifa17 = massa_altura(df_fifa17)
        df_fifa18 = pd.read_csv(pasta_datasets / 'FIFA18_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa18 = tratar_dataframe(df_fifa18)
        df_fifa18 = massa_altura(df_fifa18)
        df_fifa19 = pd.read_csv(pasta_datasets / 'FIFA19_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa19 = tratar_dataframe(df_fifa19)
        df_fifa19 = massa_altura(df_fifa19)
        df_fifa20 = pd.read_csv(pasta_datasets / 'FIFA20_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa20 = tratar_dataframe(df_fifa20)
        df_fifa20 = massa_altura(df_fifa20)
        df_fifa21 = pd.read_csv(pasta_datasets / 'FIFA21_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa21 = tratar_dataframe(df_fifa21)
        df_fifa21 = massa_altura(df_fifa21)
        df_fifa22 = pd.read_csv(pasta_datasets / 'FIFA22_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa22 = tratar_dataframe(df_fifa22)
        df_fifa23 = pd.read_csv(pasta_datasets / 'FIFA23_official_data.csv', sep = ',', decimal = '.', index_col= 0)
        df_fifa23 = tratar_dataframe(df_fifa23)
        dados = {'df_fifa17': df_fifa17,
                 'df_fifa18': df_fifa18,
                 'df_fifa19': df_fifa19,
                 'df_fifa20': df_fifa20,
                 'df_fifa21': df_fifa21,
                 'df_fifa22': df_fifa22,
                 'df_fifa23': df_fifa23}
        st.session_state['dados'] = dados

