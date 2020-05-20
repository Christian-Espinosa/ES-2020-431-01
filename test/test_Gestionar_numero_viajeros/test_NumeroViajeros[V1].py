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


from Viaje import Viaje
from Viatgers import Viatgers
from Destinos import Destinos

from API.Airhopping import User as User
from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights as Flights
from API.Airhopping import Booking as Booking
from API.Airhopping import Hotels as Hotels


##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Gestionar_numero_viajeros/


"""
- Dado un viaje con más de un viajero, el número de viajeros es el esperado


"""



class Test_NumeroViajeros(unittest.TestCase):


    Destinos_t = Destinos()
    Viajeros_t = Viatgers()

    Viajeros_t.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t.add_viatger("Anna","Dot","98765432P","20")

    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")

    Viaje_t = Viaje("v000", Viajeros_t, Destinos_t, Usuario_t)


    def test_numero_viajeros(self):

        n_viajeros = self.Viaje_t.get_num_viatgers()
        assert n_viajeros == 2
