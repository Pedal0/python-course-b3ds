# %% [markdown]
# Imports des dependences

# %%
import json

# %% [markdown]
# Jeu de donnée

# %%
with open('./data/players.json', 'r') as json_file:
    df = json.load(json_file)

# %% [markdown]
# Reorganisation du dictionnaire

# %%
df = sorted(df, key=lambda x:x["elo_points"])

# %% [markdown]
# Split du dictionnaire pour former les deux equipes

# %%
half = len(df) // 2
equipe_1 = df[:half]
equipe_2 = df[half:]
print("Equipe 1: ", equipe_1)
print("Equipe_2: ", equipe_2)

# %% [markdown]
# Boucle sur organisation du tournois

# %%
# Créer les matchmaking
matchmaking = [{'equipe_1': equipe_1[i], 'equipe_2': equipe_2[i]} for i in range(len(equipe_1))]

# %% [markdown]
# Enregistrement des données

# %%
# Enregistrer les matchmaking dans un fichier JSON
with open('./data/matchmaking.json', 'w') as file:
    json.dump(matchmaking, file, indent=4)

print("Matchmaking enregistrés")


