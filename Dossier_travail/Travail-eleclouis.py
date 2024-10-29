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
#travail de louis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
pwd

# %%
elec = pd.read_csv('./world-country-electricity.csv')

# %%
elec

# %%
elec['Country'].unique
elec['Features'] = elec['Features'].str.strip()

# %%
elec['Features'].unique()

# %%
elec1 = elec.loc[(elec['Features'] == 'distribution losses')]

# %%
elec.describe()

# %%
#Conso totales à voir sur rafael
elec_puiss = elec.loc[ elec['Features']== 'installed capacity']
elec_imp = elec.loc[ elec['Features']== 'imports']
O= elec_imp.loc[:, '1980':'2021'].columns.to_list()
Z=[pd.to_numeric(elec_imp[x], errors='coerce').sum() for x in O]
X= elec_puiss.loc[:, '1980':'2021'].columns.to_list()
Y=[pd.to_numeric(elec_puiss[x], errors='coerce').sum() for x in X]
plt.plot(X,Y)
plt.plot(O,Z)

# %%
elec_exp = elec.loc[ elec['Features']== 'exports']
O= elec_exp.loc[:, '1980':'2021'].columns.to_list()
Z=[pd.to_numeric(elec_exp[x], errors='coerce').sum() for x in O]
plt.plot(O,Z)

# %%
elec_netimp = elec.loc[ elec['Features']== 'net imports']
O= elec_imp.loc[:, '1980':'2021'].columns.to_list()
Z=[pd.to_numeric(elec_netimp[x], errors='coerce').sum() for x in O]
plt.plot(O,Z)

# %%

# %%
