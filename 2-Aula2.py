#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importando a biblioteca
import pandas as pd


# In[3]:


# Leitura dos arquivos
df1 = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/Aracaju.xlsx")
df2 = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/Natal.xlsx")
df4 = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/Recife.xlsx")
df5 = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/Salvador.xlsx")


# In[4]:


# Juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])


# In[5]:


# Exibir as 5 primeiras linhas
df.head()


# In[6]:


# Exibir as 5 últimas linhas
df.tail()


# In[7]:


# Exibir uma amostra aleatória
df.sample(5)


# In[8]:


# Veirifcar o tipo de dado de cada coluna
df.dtypes


# In[9]:


# Alterando o tipo de dado da Coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")


# In[10]:


df.dtypes


# In[11]:


# Consultando linhas com valores faltantes
df.isnull().sum()


# In[12]:


# Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)


# In[13]:


df.isnull().sum()


# In[14]:


# Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)


# In[15]:


df.isnull().sum()


# In[16]:


# Apagando as linhas com valores nulos
df.dropna(inplace=True)


# In[17]:


# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)


# In[18]:


# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)


# In[19]:


# Criando novas Colunas
df["Receita"] = df["Vendas"].mul(df["Qtde"])


# In[20]:


df.head()


# In[21]:


df["Receita/Vendas"] = df["Receita"] / df["Qtde"]


# In[22]:


df.head()


# In[23]:


# Retornando a maior receita
df["Receita"].max()


# In[24]:


# Retornando a menor receita
df["Receita"].min()


# In[25]:


# Retornando os 3 maiores valores de Receita
df.nlargest(3, "Receita")


# In[26]:


# Retornando os 3 menores valores de Receita
df.nsmallest(3, "Receita")


# In[27]:


# Agrupando por cidade
df.groupby("Cidade")["Receita"].sum()


# In[28]:


# Agrupando por cidade e ordenando os dados (do maior pro menor)
df.sort_values("Receita", ascending=False).head(10)


# In[29]:


# Trabalhando com Datas
# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")


# In[30]:


# Verificando o tipo de dado de cada coluna
df.dtypes


# In[31]:


# Transformando a coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])


# In[32]:


df.dtypes


# In[33]:


# Agrupamento por ano -- Apresentará a Receita por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()


# In[34]:


# Criando uma nova coluna de ano
df["Ano_Venda"] = df["Data"].dt.year


# In[35]:


df.sample(5)


# In[36]:


# Visualização de Dados
df["LojaID"].value_counts(ascending=False)


# In[37]:


# Gráfico de Barras
df["LojaID"].value_counts(ascending=False).plot.bar()


# In[38]:


# Gráfico de Barras Horizontais
df["LojaID"].value_counts().plot.barh()


# In[40]:


# Gráfico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()


# In[41]:


# Total de Vendas por Cidade
df["Cidade"].value_counts()


# In[44]:


# Adicionando um Título e Alterando o Nome dos Eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total Vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");


# In[45]:


# Alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total Vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");


# In[46]:


# Alterando o Estilo
plt.style.use("ggplot")


# In[47]:


df.groupby(df["mes_venda"])["Qtde"].sum().plot()
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();


# In[ ]:




