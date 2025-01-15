#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("entrer 3 phrase:")
L=list()
for i in range(3) :
 a=input(f"entrer la phrase {i+1}:")
 L.append(a)
print(L)

with open("/content/drive/MyDrive/exemple.txt","w")as fichier:
      for phrase in L:
          fichier.write(phrase+ " \n")

# with open("C:\\Users\\storm\\Bureau\\phrase.txt","r")as fichier:
#      a=fichier.readline()
#      while a:
#        print(a)
#        a=fichier.readline()

