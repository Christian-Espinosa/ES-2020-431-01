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
    precio_hotel1=0
    precio_hotel2=0
    sumPrecio2=0

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
            precio_hotel1=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=precio_hotel1
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
            precio_hotel2=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
            sumPrecio+=precio_hotel2
            sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

            Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

            Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)


    def test_viaje_add_hotel(self):

        precio = self.Viaje_t2.get_precio()        
        assert precio == float(self.sumPrecio)
        

    def test_viaje_remove_hotel(self):
         #Eliminamos hotel con ID h002
        self.Viaje_t2.remove_alojamiento("d002")
        self.sumPrecio2=self.sumPrecio-self.precio_hotel2

        precio = self.Viaje_t2.get_precio()
        assert precio == float(self.sumPrecio2)

    def test_viaje_add_coche(self):
        #Añadimos un coche en el destino con ID d002

        rc_dic2=Rentalcars.Rentalcars().buscar_coche("7351VEL")
        if rc_dic2!="No encontrado":
            c_obj_t2=Cars.Cars(rc_dic2['Matricula'], rc_dic2['precio'], 1)
            Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t2)

            sumPrecio2+=(float(rc_dic2['precio'])*int(c_obj_t2.get_dias()))


