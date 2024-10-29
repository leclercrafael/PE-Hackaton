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
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('world-country-electricity.csv')
df.info()

# %%
# On remarque que les données sont de type objet. On remplace les "--" et 'ie' par des NaN.

# On utilise donc la fonction to_numeric, avec error='coerce', qui va mettre des NaN partout où nécessaire.

for i in range (1980,2022):
    col = str(i)
    df[col] = pd.to_numeric(df[col],errors='coerce')
df.info()

# Toutes les colonnes numériques sont passées en float64.

# %%
df.describe()

# %%
# On va supprimer les espaces en trop dans les colonnes de type "object".

df.Features = df.Features.str.strip()
df.Country = df.Country.str.strip()
df.Region = df.Region.str.strip()

# %%
# On regroupe suivant le type de données d'électricité.

gen_groups = df.groupby(by=['Features']) # On regroupe les pays dans les différentes catégories.

# %%
# On peut alors avoir l'ensemble des catégories.

gen_groups.groups.keys()

# %%
########## Travail sur les pertes en 2021.

losses = gen_groups.get_group('distribution losses') # La sub-dataframe correspondant aux pertes.
# On remarque que certains pays ne renseignent plus de données au-delà d'une certaine date (URSS, Micronésie, etc.); on les repère avec isna.

losses = losses.sort_values(by='2021', ascending=False).reset_index()

# On fait le graphique des pertes (pays pour lesquelles les valeurs ne sont pas isna() ou 0.

to_be_plotted = losses[['Country','2021']][losses['2021'].notna()][losses['2021'] != 0].head(15)
to_be_plotted

# %%
# On se rend compte que l'on a trop de pays. On va se restreindre aux 10 premiers pays en termes de pertes.

to_be_plotted.head(15).plot.bar(x='Country',y='2021',ylabel='Losses in TWh')


# %%
### Quelle est la corrélation avec la production?

#import seaborn as sns

installed_cap = gen_groups.get_group('installed capacity')

installed_cap = installed_cap.sort_values(by='2021', ascending=False).reset_index()

compare = installed_cap[['Country','2021']].head(15) #Données à comparer.
compare

# %%
# On utilise la fonction relplot de seaborn.

# %pip install seaborn
import seaborn as sns

merged = pd.merge(to_be_plotted,compare,how='outer',on='Country').rename(columns={'2021_x':'Losses','2021_y':'Installed capacity'})
merged = merged.set_index('Country')
merged

# %%

# %%
sns.relplot(merged)

# %%

# %%
# COMMENTAIRES 1:

# On remarque que certains pays perdent beaucoup d'électricité par rapport à ce qu'ils ne produisent (en relatif).
# C'est le cas de pays en régions plus désertiques (Égypte, Iran, Iraq, Arabie Saoudite, Turquie). Peut-être que la chaleur augmente les pertes.

# Les plus gros producteurs sont évidemment ceux qui perdent le plus.

# Plus un pays est gros, plus on doit transporter sur de longues distances, donc on perd davantage d'énergie. C'est le cas des USA ou de la Chine.

# %%
# Graphique des pertes relatives. On crée une nouvelle colonne des pertes relatives.

merged['Rapport'] = merged['Losses']/merged['Installed capacity']
merged = merged.sort_values(by='Rapport',ascending=False)

merged[merged.Rapport.notna()].Rapport.plot.bar(ylabel='Pertes relatives')


# %%
# COMMENTAIRES 2:

# L'ordre des pays est modifié.

# On peut penser que plus les infrastructures sont vétustes, plus le pays perd de l'électricité en transport (Inde, Brésil, même la France...).

# Finalement, les gros pays tels que les USA ne sont pas les plus mauvais élèves! Tout dépend de l'infrastructure.


