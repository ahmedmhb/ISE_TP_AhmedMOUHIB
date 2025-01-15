#!/usr/bin/env python
# coding: utf-8

# In[26]:


import os

nouveau_nom = "nouveau_fichier.txt"
try:
    os.rename("/content/drive/MyDrive/exemple.txt",nouveau_nom)
    print(f"Fichier renomme en {nouveau_nom}.")
except FileNotFoundError:
    print("Le fichier a renommer n'a pas ete trouve")
except IOError:
    print("Erreur lors du renommage du fichier.")

try:
  os.remove('C:\\Users\\storm\\Bureau\\nouveau_fichier.txt')
  print("le fichier a bien ete suprime")
except FileNotFoundError:
  print("error fichier non trouve")
except IOError:
  print("Erreur lors de la suppression.")

