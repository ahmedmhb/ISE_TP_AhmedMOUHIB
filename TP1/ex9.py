# -*- coding: utf-8 -*-
"""Ex9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao6CCY_QiZWRDKAEfyfgpk9Du1oBRcGP
"""

def analyse_texte(texte):
  words = texte.split()
  caracters = len(texte)
  wordsdict = {"words": 0 , "caracters":caracters}
  i=0
  for word in words:
    wordsdict["words"] += 1
  return wordsdict
analyse_texte("hello hello im soldier boooy")