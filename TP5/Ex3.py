#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("entrer 3 phrase:")
L=list()
for i in range(3) :
 a=input(f"entrer la phrase {i+1}:")
 L.append(a)
print(L)

with open("/content/drive/MyDrive/exemple.txt","w")as fichier:
      for phrase in L:
          fichier.write(phrase+ " \n")


print("voulez vous ajouter d'autre phrase?")
reponse=input("repondre par <oui> ou <non>:")
while reponse == "oui":
     a=input(f"entrer la phrase:")
     with open("/content/drive/MyDrive/exemple.txt"ss,"a")as fichier:
          fichier.write(a+ " \n")
     print("voulez vous ajouter d'autre phrase?")
     reponse=input("repondre par <oui> ou <non>:")

