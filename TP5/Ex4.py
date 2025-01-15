#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv

with open("/content/drive/MyDrive/exemple.csv",mode='r',newline='')as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        nom,age,ville=ligne
        print("Nom:",nom,",Âge:",age,",Ville:",ville)

