#!/usr/bin/env python
# coding: utf-8

# In[3]:


def safe_division2(a, b):
  return a/b
try:
  a=5
  b=2
  safe_division(a,b)
except ZeroDivisionError:
  print("erreur de division impossible")
else:
  print("division réussie")
finally:
  print("fin du programme")

