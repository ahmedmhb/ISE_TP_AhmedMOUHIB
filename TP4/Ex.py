#!/usr/bin/env python
# coding: utf-8

# In[16]:


class vehicule:
  def __init__(self,marque,modele,annee):
    self.__marque=marque
    self.__modele=modele
    self.__annee=annee

  @property
  def marque(self):
    return self.__marque

  @marque.setter
  def marque(self,marque):
    self.__marque=marque

  @property
  def modele(self):
    return self.__modele

  @modele.setter
  def modele(self,modele):
    self.__modele=modele

  @property
  def annee(self):
    return self.__annee

  @annee.setter
  def annee(self,annee):
    self.__annee=annee

  def afficher_info(self):
    print(f"marque: {self.__marque}\nmodele: {self.__modele}\nannee: {self.__annee}\n")


class moteur:
  def __init__(self,puissance,type_moteur):
    self.__puissance=puissance
    self.__type_moteur=type_moteur

  @property
  def puissance(self):
    return self.__puissance

  @puissance.setter
  def puissance(self,puissance):
    self.__puissance=puissance

  @property
  def type_moteur(self):
    return self.__type_moteur

  @type_moteur.setter
  def type_moteur(self,type_moteur):
    self.__type_moteur=type_moteur

  def afficher_info(self):
    print(f"puissance: {self.__puissance}\ntype_moteur: {self.__type_moteur}\n")


class voiture(vehicule,moteur):
  def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_de_places):
    vehicule.__init__(self,marque,modele,annee)
    moteur.__init__(self,puissance,type_moteur)
    self.__nombre_de_places=nombre_de_places

  def afficher_info(self):
    vehicule.afficher_info(self)
    moteur.afficher_info(self)
    print(f"nombre de places: {self.__nombre_de_places}\n")

class moto(vehicule,moteur):
  def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
    vehicule.__init__(self,marque,modele,annee)
    moteur.__init__(self,puissance,type_moteur)
    self.__type_moto=type_moto

  @property
  def type_moto(self):
    return self.__type_moto

  @type_moto.setter
  def type_moto(self,type_moto):
    self.__type_moto=type_moto

  def afficher_info(self):
    vehicule.afficher_info(self)
    moteur.afficher_info(self)
    print(f"type du moto: {self.__type_moto}\n")


dadCar=voiture("opel","corsa",2011,100,"diesel",4)
dadCar.afficher_info()
motor=moto("swing","chinwa",2000,40,"melange","sport")
motor.afficher_info()

