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


from Viaje import Viaje as Viaje
from Viatgers import Viatgers
from Destinos import Destinos

from API.Airhopping import User as User
from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights as Flights
from API.Airhopping import Booking as Booking
from API.Airhopping import Hotels as Hotels

from CalcularPrecio import CalcularPrecio

##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Gestionar_Alojamientos/


"""
Dado un viaje con más de un viajero, cuando se añaden alojamientos, el precio
del viaje es el esperado

Dado un viaje con más de un viajero, cuando se quitan alojamientos, el precio
del viaje es el esperado

"""


class TestAlojamientos(unittest.TestCase):

    sumPrecio3=0
    precioHotelElim=0

    Destinos_t3 = Destinos()
    Viajeros_t3 = Viatgers()

    User_t3 = User.User()
    Usuario_t3 = User_t3.getDatosUser("787372-P")


    Viajeros_t3.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t3.add_viatger("Anna","Dot","98765432P","20")

    sc_dic3=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic3!="No encontrado":
        v_obj_t3=Flights.Flights(sc_dic3['ID'],sc_dic3['precio'])#id, precio

        bk_dic3=Booking.Booking().buscar_hotel("h001")
        if bk_dic3!="No encontrado":
            h_obj_t3=Hotels.Hotels(2, bk_dic3['ID'], 1, 1, bk_dic3['Nombre'])
            h_obj_t3.setPrecio(bk_dic3['precio'])#precio


            #Hotel + Vuelo
            sumPrecio3+=(float(bk_dic3['precio'])*int(h_obj_t3.dias)*int(h_obj_t3.numHab))
            sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))

            Destinos_t3.add_destino("d001",v_obj_t3,h_obj_t3)


    sc_dic3=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic3!="No encontrado":
        v_obj_t3=Flights.Flights(sc_dic3['ID'],sc_dic3['precio'])#id, precio

        bk_dic3=Booking.Booking().buscar_hotel("h002")
        if bk_dic3!="No encontrado":
            h_obj_t3=Hotels.Hotels(1, bk_dic3['ID'], 1, 1, bk_dic3['Nombre'])
            h_obj_t3.setPrecio(bk_dic3['precio'])#precio


            #Hotel + Vuelo
            sumPrecio3+=(float(bk_dic3['precio'])*int(h_obj_t3.dias)*int(h_obj_t3.numHab))
            precioHotelElim=(float(bk_dic3['precio'])*int(h_obj_t3.dias)*int(h_obj_t3.numHab))
            sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))

            Destinos_t3.add_destino("d002",v_obj_t3,h_obj_t3)

            Viaje_t3 = Viaje("v001", Viajeros_t3, Destinos_t3, Usuario_t3)




    def test_viaje_gestionar_alojamientos1(self):

        lista = self.Viaje_t3.get_alojamientos()
        assert len(lista) == 2


    def test_viaje_gestionar_alojamientos2(self):
        ##Elimino el hotel del destino con id d002
        self.Viaje_t3.remove_alojamiento("d002")
        lista = self.Viaje_t3.get_alojamientos()
        assert len(lista) == 1
