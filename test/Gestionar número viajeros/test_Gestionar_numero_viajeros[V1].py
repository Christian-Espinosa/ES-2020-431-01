# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:37:20 2020

@author: usuari
"""

import os
import sys
import unittest

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)

from Viatgers import Viatgers



"""
- Dado un viaje con más de un viajero, el número de viajeros es el esperado


"""


class TestViatgers(unittest.TestCase):
