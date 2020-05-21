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




#from src.GestionarMetodoPago import GestionarMetodoPago 
#from src.Viaje import Viaje
from Viatgers import Viatgers
from API.Airhopping import User
from Destinos import Destinos
from API.Vuelos import Skyscanner
from API.Vuelos import Flights
from API.Airhopping import Booking
from API.Airhopping import Hotels
from API.Coche import Rentalcars
from API.Coche import Cars
from Viaje import Viaje


"""
-Dado un viaje con múltiples destinos y más de un viajero,cuando se produce un error al realizar el pago, se reporta 
que la acción no se ha podido realizar
"""


class TestGestiondepagoV2(unittest.TestCase):

    @mock.patch('Bank.os.path')
    def test_realizarPagoV2(self):
       

        

