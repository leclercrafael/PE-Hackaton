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
#Osman RITTANO

import pandas as pd

df = pd.read_csv('world-country-electricity.csv', index_col = 'Country')
df

# %%
#Osman Rittano #on remarque que les élèments sont de type object

df.iloc[::, 0]

# %%
#Osman RITTANO

df.iloc[0, ::]

# %%
#Osman RITTANO #on accède au type avec :

df.info()

# %%
#Osman RITTANO #on somme les valeurs NaN par colonnes (par années)

df.isna().sum()

# %%
