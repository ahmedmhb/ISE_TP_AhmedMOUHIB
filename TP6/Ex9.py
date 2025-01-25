#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_positive_integer():
    while True:
        try:
            number = int(input("entez un entier positif : "))
            if number > 0:
                return number
            else:
                print("L'entier doit être positif.")
        except ValueError:
            print("Entrée invalide.")

result = get_positive_integer()
print(f"L'entier positif saisi est : {result}")

