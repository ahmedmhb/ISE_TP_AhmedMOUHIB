#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert_to_int(value):
  return int(value)
try:
  value="5,22"
  convert_to_int(value)
except ValueError:
  print("erreur de conversion impossible")

