import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
df = pd.read_csv('../Resultado.csv')

# Título do app
st.title('Visualização de Dados de Hipertensão')

# Filtro por sexo
sexo = st.sidebar.selectbox('Filtrar por Sexo', ['Todos', 'Feminino', 'Masculino'])

if sexo == 'Feminino':
    df = df[df['sexo'] == 0]
elif sexo == 'Masculino':
    df = df[df['sexo'] == 1]

# Filtro por faixa etária
idade_min, idade_max = st.sidebar.slider(
    'Selecione a faixa etária',
    min_value=int(df['idade'].min()),
    max_value=int(df['idade'].max()),
    value=(int(df['idade'].min()), int(df['idade'].max()))
)

df = df[(df['idade'] >= idade_min) & (df['idade'] <= idade_max)]


# Gráfico de Pizza: Quantidade Total de Hipertensão
st.header('Gráfico Quantidade Total de Hipertensão')
hipertensao_counts = df['previsao'].value_counts().reset_index()
hipertensao_counts.columns = ['previsao', 'count']
hipertensao_counts['previsao'] = hipertensao_counts['previsao'].map({0: 'Sem Hipertensão', 1: 'Com Hipertensão'})
fig_pizza = px.pie(hipertensao_counts, values='count', names='previsao', 
                   title='Quantidade Total de Pessoas com ou sem Hipertensão')
st.plotly_chart(fig_pizza)


# Gráfico de Linha: Quantidade total de Hipertensão ou não por Idade
st.header('Quantidade total de Hipertensão ou não por Idade')
df_grouped = df.groupby(['idade', 'previsao']).size().reset_index(name='count')
fig_linha_hipertensao = px.line(df_grouped, x='idade', y='count', color='previsao',
                               labels={'idade': 'Idade', 'count': 'Quantidade', 'previsao': 'Hipertensão'},
                               title='Quantidade total de Hipertensão ou não por Idade')
fig_linha_hipertensao.update_traces(mode='lines+markers')
st.plotly_chart(fig_linha_hipertensao)

# Gráfico de Dispersão: Frequência Cardíaca Máxima por Idade
st.header('Frequência Cardíaca Máxima por Idade')
fig_dispercao_frequencia = px.scatter(df, x='idade', y='maior_frequencia_cardiaca',
                                      labels={'idade': 'Idade', 'maior_frequencia_cardiaca': 'Frequência Cardíaca Máxima'},
                                      title='Frequência Cardíaca Máxima por Idade')
fig_dispercao_frequencia.update_traces(marker=dict(size=10, color='rgba(219, 64, 82, 0.8)', line=dict(width=2, color='rgba(219, 64, 82, 0.8)')))
st.plotly_chart(fig_dispercao_frequencia)


# Exibe o DataFrame
st.write("Dados do Arquivo CSV")
st.dataframe(df)
