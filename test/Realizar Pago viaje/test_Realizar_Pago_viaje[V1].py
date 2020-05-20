# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:38:55 2020

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

from GestionarMetodoPago import GestionarMetodoPago 



"""
-Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se
realiza correctamente, se reporta que la acción se ha realizado correctamente

"""


class TestGestiondepago(unittest.TestCase):