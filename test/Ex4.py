#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class produit:
  def __init__(self,nom,prix):
    self.__nom=nom
    self.__prix=prix
  @property
  def nom(self):
    return self.__nom
  @nom.setter
  def nom(self,nom):
    self.__nom=nom
  @property
  def prix(self):
    return self.__prix
  def price(self):
    if self.__prix > 200:
      self.__prix -= 50
      print("{} price is: {}dh \nwith a 50dh remise ✔".format(self.__nom,self.__prix))
    else:
      print("{} price is: {}dh".format(self.__nom,self.__prix))
product1=produit("livre",300)
product1.price()
product2=produit("book",150)
product2.price()

