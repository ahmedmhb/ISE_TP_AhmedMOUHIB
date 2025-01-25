#!/usr/bin/env python
# coding: utf-8

# In[3]:


class AgeNegatif(Exception):
  pass
def set_age(age):
    if age<0:
      raise AgeNegatif("age negatif")
try:
  set_age(-5)
except AgeNegatif as e:
  print(e)

