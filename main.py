import zipfile; z = zipfile.ZipFile('steam_games.zip'); 

print('\n'.join(z.namelist()[:10]))

import zipfile
import os

if not os.path.exists('data/'):
    os.makedirs('data/')

try:
    with zipfile.ZipFile('steam_games.zip', 'r') as zip_ref:
        zip_ref.extractall('data/')
except FileNotFoundError:
    pass
except Exception:
    pass



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns






### Printa as colunas para melhor organização do código

df = pd.read_csv('data/steam_games.csv')
print(df.columns)

### Converte a coluna de Data de Lançamento para o formato datetime
df['Release date'] = pd.to_datetime(df['Release date'], errors='coerce')

###melhora comunicação com coluna de Data de Lançamento
df.rename(columns={'Release date': 'release_date'}, inplace=True)

### Separa os gêneros em uma lista criando uma linha para cada gênero
df['Genres'] = df['Genres'].str.split(';').str.strip()
df_exploded_genres = df.explode('Genres')

### Converte a coluna de Pontuação Metacritic para numérico
df['Metacritic score'] = pd.to_numeric(df['Metacritic score'], errors='coerce')

# Removendo linhas onde a pontuação Metacritic é NaN, pois é o foco da P1
df.dropna(subset=['Metacritic score'], inplace=True)


