#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABC,abstractmethod
from math import pi
class forme(ABC):
  @abstractmethod
  def calculer_Surface(self,surface):
      pass
class cercle(forme):
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
class rectangle(forme):
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
  def calculer_Surface(self):
    surface=self.longueur*self.largeur
    print(surface)
cercle1=cercle(2)
cercle1.calculer_Surface()
rectangle1=rectangle(2,3)
rectangle1.calculer_Surface()

