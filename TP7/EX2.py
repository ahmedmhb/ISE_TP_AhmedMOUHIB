from os import getcwd
import time
import math

# Récupération du répertoire de travail actuel
directory = getcwd()
print(f"\ndirectory: {directory}\n")

# Récupération de l'heure et de la date actuelles
timenow = time.ctime()
print(f"\ncurrent_time: {timenow}\n")

# Calcul de la racine carrée d'un nombre saisi par l'utilisateur
racine = math.sqrt(int(input("\ntapez un nombre pour effectuer la racine\n\n")))
print(f"\n{racine}\n")
