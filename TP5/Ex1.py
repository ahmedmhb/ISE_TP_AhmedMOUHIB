#!/usr/bin/env python
# coding: utf-8

# In[10]:


with open("/content/drive/MyDrive/exemple.txt","r") as fichier:
    ligne = fichier.readline()
    i=1
    while ligne:
       print(i,ligne)
       i+=1
       ligne = fichier.readline()

