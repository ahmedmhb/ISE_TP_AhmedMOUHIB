#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import pi
class cercle:
  def __init__(self,rayon):
    self.__rayon=rayon
  @property
  def rayon(self):
    return self.__rayon
  @rayon.setter
  def rayon(self,rayon):
    self.__rayon=rayon
  def calculer_Surface(self):
    surface=pi*self.rayon**2
    print(surface)
class caree:
  def __init__(self,cote):
    self.__cote=cote
  @property
  def cote(self):
    return self.__cote
  @cote.setter
  def cote(self,cote):
    self.__cote=cote
  def calculer_surface(self):
    surface=self.cote**2
    print(surface)
class rectangle:
  def __init__(self,longueur,largeur):
    self.__longueur=longueur
    self.__largeur=largeur
  @property
  def longueur(self):
    return self.__longueur
  @longueur.setter
  def longueur(self,longueur):
    self.__longueur=longueur
  @property
  def largeur(self):
    return self.__largeur
  @largeur.setter
  def largeur(self,largeur):
    self.__largeur=largeur
  def calculer_surface(self):
    surface=self.longueur*self.largeur
    print(surface)
cercle1=cercle(2)
cercle1.calculer_Surface()
cercle2=cercle(3)
cercle2.calculer_Surface()
caree1=caree(2)
caree1.calculer_surface()
rectangle1=rectangle(2,3)
rectangle1.calculer_surface()

