#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Análise Exploratória

# Importando as Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[3]:


# Criando um novo Dataframe
df = pd.read_excel("C:/Users/evicdom/Documents/Jupyter/datasets/AdventureWorks.xlsx")


# In[4]:


# Visualizando as 5 primeiras linhas
df.head()


# In[5]:


# Criando uma Coluna com Total de Dias para Enviar o Produto
df["tempo_envio"] = df["Data Envio"] - df["Data Venda"]


# In[6]:


df.head(1)


# In[8]:


# Extraindo apenas os dias
df["tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days


# In[9]:


df.head(1)


# In[10]:


# Verificando o tipo da coluna Tempo_envio
df["tempo_envio"].dtype


# In[ ]:




