#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
  with open("/content/drive/MyDrive/inexistant.txt",'r')as fichier:
       lignes=fichier.readlines()
       print("lecture avec succes")
except FileNotFoundError:
   print('erreur fichier non trouve')
except IOError:
   print('erreur lors de lecture de fichier')

