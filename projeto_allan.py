import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="https://cdn-icons-png.flaticon.com/512/1341/1341880.png",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

# renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = pd.read_csv('C:/Users/Allan/Documents/Material de apoio/Modulo 16/projeto 2/output/renda.csv')
# renda = pd.read_csv("C:/Users/Allan/Documents/Material de apoio/Modulo 16/projeto 2/input/previsao_de_renda.csv")


#plots
renda.data_ref = pd.to_datetime(renda.data_ref)
# date_to_filter = st.slider('data', min(renda.data_ref), max(renda.data_ref), 17)  # min: 0h, max: 23h, default: 17h

min_data=renda.data_ref.min()
max_data=renda.data_ref.max()

data_inicial = st.sidebar.date_input('Data inicial', 
                value = min_data,
                min_value = min_data,
                max_value = max_data)
data_final = st.sidebar.date_input('Data final', 
                value = max_data,
                min_value = min_data,
                max_value = max_data)    



# st.sidebar.write('Data inicial = ', data_inicial)
# st.sidebar.write('Data inicial = ', data_final)


fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
# date_filter = st.slider('Data da análise', min_data, max_data, min_data)  # min: 0h, max: 23h, default: 17h

renda  = renda[(renda['data_ref'] <= pd.to_datetime(data_final)) & (renda['data_ref'] >=pd.to_datetime(data_inicial) )]

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


# plt.close('all')
# plt.rc('figure', figsize=(15, 15))
# fig, axes = plt.subplots(4, 2)
# sns.barplot(x='posse_de_imovel',y='renda',data=df, ax=axes[0,0])
# sns.barplot(x='posse_de_veiculo',y='renda',data=df, ax=axes[0,1])
# sns.barplot(x='qtd_filhos',y='renda',data=df, ax=axes[1,1])
# sns.barplot(x='sexo',y='renda',data=df, ax=axes[1,0])
# sns.barplot(x='tipo_renda',y='renda',data=df, ax=axes[2,0])
# sns.barplot(x='educacao',y='renda',data=df, ax=axes[2,1])
# sns.barplot(x='estado_civil',y='renda',data=df, ax=axes[3,0])
# sns.barplot(x='tipo_residencia',y='renda',data=df, ax=axes[3,1])

# sns.despine()





df = pd.read_csv('C:/Users/Allan/Documents/Material de apoio/Modulo 16/projeto 2/output/renda.csv')
st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
plt.xticks(rotation=90)
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
plt.xticks(rotation=90)
sns.despine()
st.pyplot(plt)



# plt.close('all')
# plt.rc('figure', figsize=(15, 15))
# fig, axes = plt.subplots(4, 2)
# sns.barplot(x='posse_de_imovel',y='renda',data=df, ax=axes[0,0])
# sns.barplot(x='posse_de_veiculo',y='renda',data=df, ax=axes[0,1])
# sns.barplot(x='qtd_filhos',y='renda',data=df, ax=axes[1,1])
# sns.barplot(x='sexo',y='renda',data=df, ax=axes[1,0])
# sns.barplot(x='tipo_renda',y='renda',data=df, ax=axes[2,0])
# sns.barplot(x='educacao',y='renda',data=df, ax=axes[2,1])
# sns.barplot(x='estado_civil',y='renda',data=df, ax=axes[3,0])
# sns.barplot(x='tipo_residencia',y='renda',data=df, ax=axes[3,1])

# sns.despine()


