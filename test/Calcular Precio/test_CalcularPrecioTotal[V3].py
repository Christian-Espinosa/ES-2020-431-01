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

##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Gestionar_Varios_Destinos/


"""
V1:
- Dado un viaje sin destinos, el precio del viaje es cero
- Dado un viaje, cuando se añaden destinos, el precio del viaje es el esperado
- Dado un viaje con más de un viajero, cuando se añaden destinos, el precio del
viaje es el esperado
- Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
destinos, el precio del viaje es el esperado

V3:
- Dado un viaje con más de un viajero, cuando se añaden vehículos, el precio del
viaje es el esperado
- Dado un viaje con más de un viajero, cuando se quitan vehículos, el precio del
viaje es el esperado
- Dado un viaje con más de un viajero, cuando se añaden alojamientos, el precio
del viaje es el esperado
- Dado un viaje con más de un viajero, cuando se quitan alojamientos, el precio
del viaje es el esperado

"""


class TestCalcularPrecioTotalV1(unittest.TestCase):


####Dado un viaje sin destinos
    Destinos_t = Destinos()
    Viajeros_t = Viatgers()

    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")

    Viaje_t = Viaje("v000", Viajeros_t, Destinos_t, Usuario_t)


####Se añaden Destinos
    sumPrecio=0

    Destinos_t2 = Destinos()
    Viajeros_t2 = Viatgers()

    User_t2 = User.User()
    Usuario_t2 = User_t2.getDatosUser("787372-P")

    Viajeros_t2.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t2.add_viatger("Anna","Dot","98765432P","20")

    sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic2!="No encontrado":
        v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

        #Añadir Hotel
        bk_dic2=Booking.Booking().buscar_hotel("h001")
        if bk_dic2!="No encontrado":
            h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
            h_obj_t2.setPrecio(bk_dic2['precio'])#precio

            #Hotel + Vuelo
            sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

            Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)


    sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic2!="No encontrado":
        v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio


        #Añadir Hotel
        bk_dic2=Booking.Booking().buscar_hotel("h002")
        if bk_dic2!="No encontrado":
            h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
            h_obj_t2.setPrecio(bk_dic2['precio'])#precio

            #Hotel + Vuelo
            sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

            Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

            Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)

    def test_viaje_add_hotel(self):

        precio = self.Viaje_t2.get_precio()
        assert precio == float(self.sumPrecio)

    #Eliminamos hotel con ID h002
    Viaje_t2.remove_alojamiento("h002")
    sumPrecio-=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
    def test_viaje_remove_hotel(self):

        precio = self.Viaje_t2.get_precio()
        assert precio == float(self.sumPrecio)



####Cuando se quitan destinos
    sumPrecio3=0

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

            #sumPrecio3=sumPrecio3+float(sc_dic3['precio'])+float(bk_dic3['precio'])

            #Hotel + Vuelo
            sumPrecio3+=(float(bk_dic3['precio'])*int(h_obj_t3.dias)*int(h_obj_t3.numHab))
            sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))

            Destinos_t3.add_destino("d002",v_obj_t3,h_obj_t3)

            Viaje_t3 = Viaje("v001", Viajeros_t3, Destinos_t3, Usuario_t3)


    Viaje_t3.remove_destino("d001")

    sp3=CalcularPrecio(Viajeros_t3,Destinos_t3)
    sumPrecio3=sp3.calc_precio()

    def test_viaje_add_hotel(self):

        precio = self.Viaje_t3.get_precio()
        assert precio == float(self.sumPrecio3)
    
    def test_viaje_rm_hotel(self):
