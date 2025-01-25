#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_positive_integer():
  try:
    number = int(input("Veuillez saisir un entier positif : "))
    if number > 0:
      return number
    else:
      print("L'entier doit être positif.")
  except ValueError:
    print("Entrée invalide, veuillez saisir un entier.")

def lire_fichier():
  try:
    file_name = input("Veuillez saisir le nom du fichier : ")
    with open(file_name, 'r') as file:
      print("Fichier ouvert avec succès.")
      content = file.read()
      print("Contenu du fichier :")
      print(content)
  except FileNotFoundError:
    print("Erreur : le fichier n'existe pas.")
  except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")

number = get_positive_integer()
print(number)

