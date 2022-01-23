""" Dados Enem 2019 """

import pandas as pd

fonte = r'C:\MICRODADOS_ENEM_2019_SAMPLE_43278.csv'

import seaborn as sns
import matplotlib.pyplot as plt


dados = pd.read_csv()  # read é a variável para o pandas ler o arquivo csv
dados.head()  
dados.shape()  # Toda extrutura do arquivo, QNT de linhas e colunas

dados["SG_UF_RESIDENCIA"]  # Selecionando a coluna de dados que quero analizar, em uma lista
dados.columns.values  # Retorna todas as colunas do dataframe
dados["SG_UF_RESIDENCIA"].unique()  # seleciona todos os estados mas não repete nenhum
len(dados["SG_UF_RESIDENCIA"].value_counts())  # quantidade de estados, 27 por exemplo

#Vamos ver outras informações como a questão das idades dos candidatos

dados["NU_IDADE"].hist()  # visualização de dados do pandas em formato de gráficos
dados["NU_IDADE"].hist(bins=30)  # Aumenta as informações com mais ranges dos dados
dados["NU_IDADE"].hist(bins=30, figsize=(10, 8))  # figsize vai formatar o tamanho da imagem

dados.query("IN_TREINEIRO == 1")  # Vai me mostrar apenas quem é treineiro
dados.query("IN_TREINEIRO == 1")["NU_IDADES"].value_counts()  # Quantidade de Treineiros por idade

dados["NU_NOTA_REDACAO"].mean()  # Média da nota da redação
dados["NU_NOTA_REDACAO"].std()  # Desvio Padrão

#Vamos criar uma variável provas, para compararmos as notas

provas = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
dados[provas].describe()  # Vai mostrar uma tabela das inf. estatístivas do pandas
dados["NU_NOTA_CN"].quantile(0.9)  # retorna 10% das notas mais altas, para as mais baixas usariamos (0.1)

dados["NU_NOTA_CN"].plot.box(grid=True, figsize=(8, 6))
# Normalmente o boxplot é demonstrado em conjunto com outras notas, para facilitar a comparação visual.

#Quantos alunos com 14 anos ou menos temos por estado, e qual é a proporção?
dados.query("NU_IDADE <= 14")["SG_UF_RESIDENCIA"].value_counts(normalize=True)

# Para construirmos um gráfico com essa informação, seguimos abaixo:
alunos_menor_quatorze = dados.query("NU_IDADE <= 14")
alunos_menor_quatorze["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.pie(figsize=(10, 8))  # Gráfico de pizza
alunos_menor_quatorze["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.bar(figsize=(10, 8))  # Gráfico de barras

plt.figure(figsize=(10, 8))  # Formatando o tamanho do gráfico pelo matplotlib.pyplot
renda_ordenada = dados['Q006'].unique()  # Ordenando as informações do eixo Y, vamos precisar usar o SORT na variável
renda_ordenada.sort()
sns.boxplot(x='Q006', y='NU_NOTA_MT', data=dados, order=renda_ordenada)  # Gráfico boxplot importado do seaborn
plt.title("Boxplot das notas de Matemática pela renda")  # pedindo ao matplotlib para incluir um título

dados[provas].sum(axis=1)  # Somando as notas de todas as provas do eixo '1', que é das linhas. Colunas é o eixo '0'
dados["NU_NOTAS_TOTAL"] = dados[provas].sum(axis=1)  # INCLUINDO UMA NOVA COLUNA NO NOSSO DATAFRAME(DADOS)
dados.head()  # Visualizando o dataframe

#Criamos então o mesmo gráfico boxplot para vizualizarmos todas as notas
plt.figure(figsize=(10, 8))
renda_ordenada = dados['Q006'].unique()
renda_ordenada.sort()
sns.boxplot(x='Q006', y='NU_NOTA_TOTAL', data=dados, order=renda_ordenada)
plt.title("Boxplot do total das notas pela renda")

provas.append('NU_NOTA_TOTAL')
dados[provas].query('NU_NOTA_TOTAL == 0')  # Para encontrarmos todas as pessoas com nota == 0

dados_sem_nota_zero = dados[provas].query('NU_NOTA_TOTAL != 0')  # Nova variável, apenas com que teve nota
dados_sem_nota_zero.head()
sns.boxplot(x='Q006', y='NU_NOTA_TOTAL', data=dados_sem_nota_zero, order=renda_ordenada)
plt.title("Boxplot do total das notas pela renda")

#Vamos incluir mais uma variável na análise do boxplot, usando a função 'hue'
plt.figure(figsize=(10, 8))
renda_ordenada = dados['Q006'].unique()
renda_ordenada.sort()
sns.boxplot(x='Q006', y='NU_NOTA_TOTAL', data=dados_sem_nota_zero, hue='IN_TREINEIRO', order=renda_ordenada)
plt.title("Boxplot do total das notas pela renda")
