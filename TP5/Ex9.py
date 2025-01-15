#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('/content/drive/MyDrive/journal.txt','r')as fichier:
    lignes=fichier.readlines()
    nbr_de_ligne=len(lignes)
    print("nombre de ligne:",nbr_de_ligne)

    nbe_de_mot = 0
    nbr_de_caractere = 0
    for ligne in lignes:
     nbe_de_mot += len(ligne.split())
     nbr_de_caractere += len(ligne)

    print("nombre de mot:",nbe_de_mot)
    print("nombre de caractere:",nbr_de_caractere)

