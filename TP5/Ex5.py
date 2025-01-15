#!/usr/bin/env python
# coding: utf-8

# In[23]:


import json

dict = {
         "E0": {"nom": "Ayoub", "age": 22, "note": 16},
    "E1": {"nom": "Mohammed", "age": 21, "note": 14.5},
       "E2": {"nom": "Ali", "age": 20, "note": 13}
}



with open("/content/drive/MyDrive/exemple.json","w") as fichier:
    json.dump(dict, fichier, indent=4)

with open("/content/drive/MyDrive/exemple.json",'r') as fichier:
    donnees = json.load(fichier)

for etudiant, info in donnees.items():
        print("nom:", info["nom"],"age:",info["age"],"note:",info["note"])

