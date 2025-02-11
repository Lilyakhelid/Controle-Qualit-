# %%

#--importer les librairies--
import pandas as pd
import os

#--Lire le fichier de données--
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
file_path = os.path.join(base_dir, 'data', 'raw', 'mes_bfc_quotidienne_poll_princ.csv')

df = pd.read_csv(file_path)

# %%

#--Filtrer les données--


df['nom_dept'] = df['nom_dept'].astype(str)
#--Ville de naissance--
df = df[df['nom_com']== 'Vesoul'] 
#--Particule la plus respnsable de l'asthme--
df = df[df['nom_poll']== 'PM2.5']
#--Sur deux ans apres la naissance--
df['date_debut'] = pd.to_datetime(df['date_debut'])
df['date_fin'] = pd.to_datetime(df['date_fin'])

df = df[(df['date_debut'].dt.year > 2022) 
        & (df['date_fin'].dt.year <= 2024)]
#--Pour une fiabilité--
df = df[df['statut_valid']== True]
#--on ne prend uniquement les colonnes ou il n'y a pas que un seul element dedans & utile--
df = df[['date_debut', 'date_fin', 'valeur']]

# %%

save_path = os.path.join(os.path.dirname(os.getcwd()), "data", "processed", "Vesoul_PM2.5_2022_2024.csv")

df.to_csv(save_path, index=False)

# %%
