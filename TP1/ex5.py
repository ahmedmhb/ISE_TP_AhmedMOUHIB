# -*- coding: utf-8 -*-
"""Ex5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao6CCY_QiZWRDKAEfyfgpk9Du1oBRcGP
"""

def factorielle(n):
  if n == 0:
    return 1
  else:
    return n * factorielle(n-1)
factorielle(9)