# -*- coding: utf-8 -*-
"""Ex4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao6CCY_QiZWRDKAEfyfgpk9Du1oBRcGP
"""

def compte_occurences(liste):
  occurences = {}
  for element in liste:
    if element in occurences:
      occurences[element] += 1
    else:
      occurences[element] = 1
  return occurences
compte_occurences(['Ahmed', 'Brahim', 'Fati', 'Brahim', 'Fati', 'Hamid', 'Fati' ,'Imane'])