import pandas as pd

# Charger le fichier CSV
data = pd.read_csv("C:\\Users\\Administrateur\\Desktop\\employees.csv")

# Afficher le nom et l'âge des 4 premiers employés
for i in range(0, 4):
    print(f"{data.loc[i]['Name']}: {data.loc[i]['Age']}")

# Calculer et afficher la moyenne des âges
print(f"Moyenne d'âge: {data['Age'].mean()}")
