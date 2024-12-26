#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class commande:
  def __init__(self,nom,prix,quantite):
    self.__nom=nom
    self.__prix=prix
    self.__quantite=quantite
  @property
  def nom(self):
    return self.__nom
  @nom.setter
  def nom(self,nom):
    self.__nom=nom
  @property
  def prix(self):
    return self.__prix
  @prix.setter
  def prix(self,prix):
    self.__prix=prix
  @property
  def quantite(self):
    return self.__quantite
  @quantite.setter
  def quantite(self,quantite):
    self.__quantite=quantite
  panier={}
  def add_commande(self):
    if self.nom in self.panier:
      self.panier[self.nom]+=self.quantite
    else:
      self.panier[self.nom]=self.quantite
  def afficher_panier(self):
    print(self.panier)
tele=commande("iPhone 9000",6000,2)
tele.add_commande()
tele.afficher_panier()
rechaud=commande("Prima",200,1)
pc=commande("HP",5000,1)
rechaud.add_commande()
pc.add_commande()
pc.afficher_panier()
pc.add_commande()
pc.afficher_panier()

