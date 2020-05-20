# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:38:18 2020

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

from Destinos import Destinos



"""
- Dado un viaje sin destinos, la lista de destinos está vacía
- Dado un viaje, cuando se añaden destinos, la lista de destinos es la esperada
- Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
destinos, la lista de destinos es la esperada

"""


class TestDestino(unittest.TestCase):