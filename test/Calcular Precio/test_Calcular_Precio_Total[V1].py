# -*- coding: utf-8 -*-
"""
Created on Wed May 20 03:53:12 2020

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
from CalcularPrecio import CalcularPrecio

"""
- Dado un viaje sin destinos, el precio del viaje es cero
- Dado un viaje, cuando se añaden destinos, el precio del viaje es el esperado
- Dado un viaje con más de un viajero, cuando se añaden destinos, el precio del
viaje es el esperado
- Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
destinos, el precio del viaje es el esperado
"""
