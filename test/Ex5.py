#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class employe:
  def __init__(self,nom,prenom,salaire):
    self.__nom=nom
    self.__prenom=prenom
    self.__salaire=salaire
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
  def salaire(self):
    return self.__salaire
  def salarie(self):
    self.__employe="{} + {}: {}".format(self.__nom,self.__prenom,self.__salaire)
    return self.__employe
  @property
  def employe(self):
    return self.__employe
  @employe.setter
  def employe(self,employes):
    self.__employe=employe
class manager(employe):
  def __init__(self,nom,prenom,salaire):
    super().__init__(nom,prenom,salaire)
  __employes=[]
  @property
  def employes(self):
    return self.__employes
  @employes.setter
  def employes(self,employes):
    self.__employes=employes
  def add_employe(self):
    if self.employe not in self.employes:
      self.employes.append(self.employe)
    print(f"employes supervises par manager: {self.employes}")
employe1=manager("ahmed","mouhib",7000)
employe1.salarie()
employe1.add_employe()
employe2=manager("mohamed","mouhib",8000)
employe2.salarie()
employe2.add_employe()

