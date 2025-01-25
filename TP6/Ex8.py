#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest
from logs import log_error
class testing(unittest.TestCase):
    def test_log_error(self):
        self.assertEqual(log_error("FileNotFoundError"), "ERROR:root:FileNotFoundError")
unittest.main()

