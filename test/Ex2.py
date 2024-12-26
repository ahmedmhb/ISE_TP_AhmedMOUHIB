#!/usr/bin/env python
# coding: utf-8

# In[1]:


class personne:
  def __init__(self,nom,prenom,age):
    self.__nom=nom
    self.__prenom=prenom
    self.__age=age
  @property
  def nom(self):
    return self.__nom
  @nom.setter
  def nom(self,nom):
    self.__nom=nom
  @property
  def prenom(self):
    return self.__prenom
  @prenom.setter
  def prenom(self,prenom):
    self.__prenom=prenom
  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self,age):
    self.__age=age
  def afficher(self):
    print(self.nom,self.prenom,self.age)
personne1=personne("ahmed","mouhib",21)
personne1.afficher()
personne2=personne("mohamed","mouhib",22)
personne2.afficher()

