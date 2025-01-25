#!/usr/bin/env python
# coding: utf-8

# In[2]:


try:
  fichier = open("/content/drive/MyDrive/exemple.txt","r")
  ligne = fichier.readline()
except:
  print("erreur : fichier introuvable")
finally:
  fichier.close()

