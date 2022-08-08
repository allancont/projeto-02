import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


import warnings
warnings.filterwarnings('ignore')

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon='https://imagepng.org/wp-content/uploads/2019/05/dinheiro-icone-6.png',
     layout="wide",
)

df_coef = pd.read_csv("C:/Users/Allan/Documents/Material de apoio/Modulo 16/projeto 2/output/coeficientes.csv")
                      

st.title("SIMULAÇÃO DE RENDA")

# contact_options = ['Feminino', 'Masculino']

# st.header('Informe o gênero')


st.write('----')
# st.title("Make a Radio Button")
op_genero = ['Masculino', 'Feminino']
genero = st.radio('Gênero', op_genero,horizontal=True)
def _genero(n):
    if n == 'Masculino':
        return 1
    return 0

st.write('----')
#Barra de arraste
op_tempo_emprego = st.slider('Tempo de emprego',
    min_value=0.0,
    max_value=40.0,
    value=1.0,
    step=0.5)
# st.write("você selecionou: ",op_tempo_emprego)

st.write('----')
op_empresario = ['Sim', 'Não']
empresario = st.radio('Empresário?', op_empresario,horizontal=True)
def _empresario(n):
    if n == 'Sim':
        return 1
    return 0


st.write('----')
op_imovel = ['Sim', 'Não']
imovel = st.radio('Possui imóvel?', op_imovel,horizontal=True)
def _imovel(n):
    if n == 'Sim':
        return 1
    return 0

st.write('----')
op_superior = ['Sim', 'Não']
superior = st.radio('Ensino superior completo?', op_superior,horizontal=True)
def _superior(n):
    if n == 'Sim':
        return 1
    return 0

st.write('----')
op_idade = st.slider('Idade',
    min_value=18,
    max_value=90,
    value=18,
    step=1)
# st.write("você selecionou: ",op_idade)

# st.write('----')
# op_pessoas = st.slider('Quantidade de pessoas na residência',
#     min_value=1,
#     max_value=20,
#     value=1,
#     step=1)
# # st.write("você selecionou: ",op_pessoas)
st.write('----')
st.header('Confira suas respostas')
st.write('Gênero:',genero)
st.write('Idade:',op_idade)
st.write('Tempo de emprego:',op_tempo_emprego)
st.write('Empresário?',empresario)
st.write('Possui imóvel?',imovel)
st.write('Curso superior?',superior)
# st.write('Quantidade de pessoas na residência:',op_pessoas)
st.write('----')

st.title("Cálculo da renda")
result = st.button ("CALCULAR")
# st.write(result)
if result:
    resultado_renda = (df_coef['Intercept'] + 
    (df_coef['tempo_emprego'] * op_tempo_emprego) + 
    (df_coef['sexo_M'] * _genero(genero))+ 
    (df_coef['tipo_renda_Empresário'] * _empresario(empresario)) + 
    (df_coef['posse_de_imovel_True'] * _imovel(imovel)) +
    (df_coef['educacao_Superior_completo'] * _superior(superior) ) +
    (df_coef['idade'] * op_idade ) 
    # +(df_coef['qt_pessoas_residencia'] * op_pessoas)
    )
    resultado = round(np.exp(resultado_renda),2)
    st.metric(label="Renda prevista", value=resultado)
    # st.metric(label="Renda coeficiente", value=round(resultado_renda,4))


# st.write('----')
# st.header('Confira as principais variáveis')
# st.write(df_coef['Intercept'])
# st.write('Tempo de emprego:',(df_coef['tempo_emprego'] * op_tempo_emprego))
# st.write('Gênero:',df_coef['sexo_M'] * _genero(genero))
# st.write('Empresário?',df_coef['tipo_renda_Empresário'] * _empresario(empresario))
# st.write('Possui imóvel?',df_coef['posse_de_imovel_True'] * _imovel(imovel))
# st.write('Curso superior?',df_coef['educacao_Superior_completo'] * _superior(superior))
# st.write('Idade:',df_coef['idade'] * op_idade )
# # st.write('Quantidade de pessoas na residência:',df_coef['qt_pessoas_residencia'] * op_pessoas)


st.write('----')




st.write('# Análise exploratória da previsão de renda')

result = st.button ("EXIBIR GRÁFICOS")
if result:
    renda = pd.read_csv("C:/Users/Allan/Documents/Material de apoio/Modulo 16/projeto 2/output/renda.csv")
                         
    fig, ax = plt.subplots(8,1,figsize=(10,70))
    renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
    st.write('## Gráficos ao longo do tempo')
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
    ax[1].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
    ax[2].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
    ax[3].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
    ax[4].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
    ax[5].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
    ax[6].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
    ax[7].tick_params(axis='x', rotation=45)
    sns.despine()
    st.pyplot(plt)

    st.write('## Gráficos bivariada')
    fig, ax = plt.subplots(7,1,figsize=(10,50))
    sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
    sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
    sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
    sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
    sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
    sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
    sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
    sns.despine()
    st.pyplot(plt)


