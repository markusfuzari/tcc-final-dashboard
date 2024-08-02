import streamlit as st
import pickle
import pandas as pd

# Carregar o modelo
with open('./data/modelo_paciente_hipertensao.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Função para fazer predições
def fazer_predicao(dados):
    predicoes = modelo.predict(dados)
    return predicoes

# Interface do usuário no Streamlit
st.title('Previsão de Hipertensão')

# Campos de entrada para o usuário
idade = st.number_input('Idade')
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
tipo_dor = st.selectbox('Tipo de Dor no Peito', [1, 2, 3, 4])
pressao_sanguinea = st.number_input('Pressão Sanguínea em Repouso')
colesterol = st.number_input('Colesterol')
nivel_acucar = st.selectbox('Nível de Açúcar no Sangue em Jejum', [0, 1])
ecg = st.selectbox('Resultados do ECG em Repouso', [0, 1, 2])
max_freq_cardiaca = st.number_input('Frequência Cardíaca Máxima Alcançada')
angina_exercicio = st.selectbox('Angina Induzida pelo Exercício', [0, 1])
depressao_st = st.number_input('Depressão do Segmento ST Induzida por Exercício')
slope_st = st.selectbox('Inclinação do Segmento ST Pico de Exercício', [1, 2, 3])
vasos = st.number_input('Número de Vasos Coloridos por Fluoroscopia')
defeito = st.selectbox('Defeito Reversível ou Fixo', [3, 6, 7])

# Criar um DataFrame com os dados inseridos
dados_usuario = pd.DataFrame({
    'idade': [idade],
    'sexo': [1 if sexo == 'Masculino' else 0],
    'tipo_de_dor': [tipo_dor],
    'pressao_sanguinea': [pressao_sanguinea],
    'colesterol': [colesterol],
    'nivel_acucar': [nivel_acucar],
    'ecg': [ecg],
    'max_freq_cardiaca': [max_freq_cardiaca],
    'angina_exercicio': [angina_exercicio],
    'depressao_st': [depressao_st],
    'slope_st': [slope_st],
    'vasos': [vasos],
    'defeito': [defeito]
})

# Fazer predição
if st.button('Fazer Previsão'):
    resultado = fazer_predicao(dados_usuario)
    st.write(f'Predição: {resultado[0]}')
