#!/usr/bin/env python
# coding: utf-8

# In[3]:


def process_input(user_input):
  return (10/(int(input(user_input))))
try:
  process_input("donner un nombre")
except ValueError:
  print("erreur de conversion impossible")
except ZeroDivisionError:
  print("erreur de division impossible")

