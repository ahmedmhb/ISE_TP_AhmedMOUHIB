# -*- coding: utf-8 -*-
"""EX4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1etZll9LYgO5uf2LaS6ZevZOIDguhio8k
"""

class animal:
  def __init__(self):
    pass
  def faire_de_bruit(self,type):
    print(f"{type} fais du bruit")
class chien(animal):
  def __init__(self):
    super().__init__()
class chat(animal):
  def __init__(self):
    super().__init__()
cat=chat()
cat.faire_de_bruit('cat')