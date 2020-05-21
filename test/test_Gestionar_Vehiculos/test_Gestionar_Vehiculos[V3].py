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

##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Gestionar_Vehiculos/


"""
Dado un viaje con más de un viajero, cuando se añaden vehículos, el precio del
viaje es el esperado

Dado un viaje con más de un viajero, cuando se quitan vehículos, el precio del
viaje es el esperado

"""


class TestDestino(unittest.TestCase):


####Dado un viaje sin destinos
    Destinos_t = Destinos()
    Viajeros_t = Viatgers()

    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")

    Viaje_t = Viaje("v000", Viajeros_t, Destinos_t, Usuario_t)


    def test_viaje_sin_destinos_listaDestinos(self):

        listaDestinos = self.Viaje_t.get_destinos()
        assert len(listaDestinos) == 0


    def test_viaje_sin_destinos_listaVuelos(self):

        listaVuelos = self.Viaje_t.get_vuelos()
        assert len(listaVuelos) == 0




####Cuando se añaden Destinos
    sumPrecio=0

    Destinos_t2 = Destinos()
    Viajeros_t2 = Viatgers()

    User_t2 = User.User()
    Usuario_t2 = User_t2.getDatosUser("787372-P")

    #Viaje_t2 = Viaje.Viaje(0, Viajeros_t2, Destinos_t2, Usuario_t2)

    Viajeros_t2.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t2.add_viatger("Anna","Dot","98765432P","20")

    sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic2!="No encontrado":
        v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

        bk_dic2=Booking.Booking().buscar_hotel("h001")
        if bk_dic2!="No encontrado":
            h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
            h_obj_t2.setPrecio(bk_dic2['precio'])#precio

            #sumPrecio=sumPrecio+float(sc_dic2['precio'])+float(bk_dic2['precio'])

            #Hotel + Vuelo
            sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

            Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)


    sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic2!="No encontrado":
        v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

        bk_dic2=Booking.Booking().buscar_hotel("h002")
        if bk_dic2!="No encontrado":
            h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
            h_obj_t2.setPrecio(bk_dic2['precio'])#precio

            #sumPrecio=sumPrecio+float(sc_dic2['precio'])+float(bk_dic2['precio'])

            #Hotel + Vuelo
            sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

            Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

            Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)


    def test_viaje_con_destinos_listaDestinos(self):

        listaDestinos = self.Viaje_t2.get_destinos()
        assert len(listaDestinos) == 2


    def test_viaje_con_destinos_listaVuelos(self):

        listaVuelos = self.Viaje_t2.get_vuelos()
        assert len(listaVuelos) == 2





####Cuando se quitan destinos
    sumPrecio3=0

    Destinos_t3 = Destinos()
    Viajeros_t3 = Viatgers()

    User_t3 = User.User()
    Usuario_t3 = User_t3.getDatosUser("787372-P")

    #Viaje_t2 = Viaje.Viaje(0, Viajeros_t2, Destinos_t2, Usuario_t2)

    Viajeros_t3.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t3.add_viatger("Anna","Dot","98765432P","20")

    sc_dic3=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic3!="No encontrado":
        v_obj_t3=Flights.Flights(sc_dic3['ID'],sc_dic3['precio'])#id, precio

        bk_dic3=Booking.Booking().buscar_hotel("h001")
        if bk_dic3!="No encontrado":
            h_obj_t3=Hotels.Hotels(2, bk_dic3['ID'], 1, 1, bk_dic3['Nombre'])
            h_obj_t3.setPrecio(bk_dic3['precio'])#precio

            #sumPrecio3=sumPrecio3+float(sc_dic3['precio'])+float(bk_dic3['precio'])

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

            #sumPrecio3=sumPrecio3+float(sc_dic3['precio'])+float(bk_dic3['precio'])

            #Hotel + Vuelo
            sumPrecio3+=(float(bk_dic3['precio'])*int(h_obj_t3.dias)*int(h_obj_t3.numHab))
            sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))

            Destinos_t3.add_destino("d002",v_obj_t3,h_obj_t3)

            Viaje_t3 = Viaje("v001", Viajeros_t3, Destinos_t3, Usuario_t3)


    Viaje_t3.remove_destino("d001")

    sp3=CalcularPrecio(Viajeros_t3,Destinos_t3)
    sumPrecio3=sp3.calc_precio()

    def test_viaje_con_destinos_listaDestinos2(self):

        listaDestinos = self.Viaje_t3.get_destinos()
        assert len(listaDestinos) == 1


    def test_viaje_con_destinos_listaVuelos2(self):

        listaVuelos = self.Viaje_t3.get_vuelos()
        assert len(listaVuelos) == 1
