#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[12]:


df = pd.read_csv("C:/Users/evicdom/Documents/Jupyter/datasets/Gapminder.csv", error_bad_lines=False, sep=";")


# In[13]:


# Visualizando as 5 primeiras linhas:
df.head()


# In[25]:


# Trocar nome das Colunas
df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de Vida", "pop":"Pop Total", "gdpPercap":"PIB"})


# In[26]:


# Colocar o resultado na troca de nomes na variável df
df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de Vida", "pop":"Pop Total", "gdpPercap":"PIB"})


# In[27]:


# Exibir as 10 primeiras linhas
df.head()


# In[28]:


# Exibir o total de Linhas e Colunas
df.shape


# In[29]:


# Exibir somente o nome das Colunas
df.columns


# In[30]:


# Exibir o tipo de Dado em cada Coluna
df.dtypes


# In[31]:


# Exibir as últimas linhas
df.tail()


# In[32]:


# Exibir Informações Estatísticas para os dados de cada coluna
df.describe()


# In[34]:


# Como fazer um filtro
# Verificar quais os continentes temos na base
df["Continente"].unique()


# In[35]:


# Fazer um filtro para exibir somente os valores referente ao continente Oceania
Oceania = df.loc[df["Continente"] == "Oceania"]
Oceania.head()


# In[37]:


# Agrupamento de Dados
# Agrupar por continente e realizar uma contagem distinta
df.groupby("Continente")["Pais"].nunique()


# In[38]:


# Agrupar informando em cada ano qual expectativa de vida média em caada pai
df.groupby("Ano")["Expectativa de Vida"].mean()


# In[39]:


# Fazer a Média da Coluna PIB
df["PIB"].mean()


# In[40]:


# Fazer Soma da Coluna PIB
df["PIB"].sum()


# In[ ]:




