# -*- coding: utf-8 -*-
"""EX4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1etZll9LYgO5uf2LaS6ZevZOIDguhio8k
"""

class personne:
  def __init__(self,ami):
    self.ami=ami
  liste=[]
  def ajouter_ami(self):
    self.liste.append(self.ami)
  def afficher_amis(self):
    print(self.liste)
ami1=personne("Ahmed")
ami1.ajouter_ami()
ami1.afficher_amis()