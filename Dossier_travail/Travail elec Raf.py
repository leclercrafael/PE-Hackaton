# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
#Travail de Rafaël
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# On va observer la dataframe :

# %%
df = pd.read_csv('world-country-electricity.csv', na_values=['--', 'ie','nan'])
df

# %%
for x in df['2012']:
    try:
        float(x)
    except:
        print(x)

# %%
df['Features']=df['Features'].str.strip()
df['Country']=df['Country'].str.strip()
df['Region']=df['Region'].str.strip()

# %% [markdown]
# Quelles sont les différentes catégories de notre dataframe ?

# %%
df['Features'].unique()

# %% [markdown]
# On va commencer par observer quelques graphiques pour voir les tendances globales, les consommations globales par exemple

# %%
df_conso=df.loc[df['Features']== 'net consumption']
X=df_conso.loc[:,'1980':'2021'].columns.to_list()
Y=[pd.to_numeric(df_conso[x], errors='coerce').sum() for x in X]
plt.plot(X,Y)
plt.xlabel('Année de 1988 à 2021')
plt.ylabel('Consommation mondiale en TWh')
plt.grid()

# %% [markdown]
# On observe bien une augmentation globale ce qui est parfaitement cohérent

# %% [markdown]
# On va étudier l'évolution de la consomation pour chaque région du Monde

# %%
df['Region'].unique()

# %%
years = df_conso.columns[3:]
df_conso.pivot_table( index=years, columns=df_conso['Region'].unique(), aggfunc='sum')

# %%
df_conso.loc[:,'1980':'2021']

# %%
df_conso.groupby(by='Region').sum().loc[:,'1980':'2021'].T.plot()

# %%
