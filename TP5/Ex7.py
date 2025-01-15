#!/usr/bin/env python
# coding: utf-8

# In[27]:


import shutil
source = "/content/drive/MyDrive/journal.txt"
destination = "/content/drive/MyDrive/journal_copie.txt"

try:
    shutil.copy(source,destination)
    print(f"Fichier copie de {source} a {destination}.")
except FileNotFoundError:
    print("fichier non trouve")
except IOError:
    print("Erreur de copy")

source = "fichier_a_deplacer.txt"
destination = "nouveau_dossier/fichier_deplace.txt"

try:
    shutil.move("/content/drive/MyDrive/journal.txt","/content/drive/MyDrive/journal_copie.txt")
    print("Fichier déplacé.")
except FileNotFoundError:
    print("Le fichier à déplacer n'a pas été trouvé.")
except IOError:
    print("Erreur lors du déplacement du fichier.")

