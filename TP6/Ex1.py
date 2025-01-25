#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def safe_division(a, b):
  return a/b
try:
  a=5
  b=2
  safe_division(a,b)
except ZeroDivisionError:
  print("erreur de division impossible")

