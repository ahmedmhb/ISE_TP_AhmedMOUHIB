#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC,abstractmethod
class Vehicule(ABC):
  def deplacer(self):
    pass
class Voiture(Vehicule):
  def deplacer(self):
    print("la voiture roule")
class bicyclette(Vehicule):
  def deplacer(self):
    print("la bicyclette roule")
bicyclette1=bicyclette()
bicyclette1.deplacer()
voiture1=Voiture()
voiture1.deplacer()

