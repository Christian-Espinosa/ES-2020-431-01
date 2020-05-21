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

from API.Coche import Rentalcars as Rentalcars
from API.Coche import Cars as Cars

##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Gestionar_Vehiculos/


"""
Dado un viaje con más de un viajero, cuando se añaden vehículos, el precio del
viaje es el esperado

Dado un viaje con más de un viajero, cuando se quitan vehículos, el precio del
viaje es el esperado

"""


class TestVehiculos(unittest.TestCase):


####Cuando se añaden vehiculos
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

        sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))
        Destinos_t2.add_destino("d001",v_obj_t2,None)

        rc_dic2=Rentalcars.Rentalcars().buscar_coche("1234ABC")
        if rc_dic2!="No encontrado":
            c_obj_t2=Cars.Cars(rc_dic2['Matricula'], rc_dic2['precio'], 1)
            Destinos_t2.get_destino("d001").set_vehiculo(c_obj_t2)

            sumPrecio+=(float(rc_dic2['precio'])*int(c_obj_t2.get_dias()))




    sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic2!="No encontrado":
        v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

        sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))
        Destinos_t2.add_destino("d002",v_obj_t2,None)

        rc_dic2=Rentalcars.Rentalcars().buscar_coche("7351VEL")
        if rc_dic2!="No encontrado":
            c_obj_t2=Cars.Cars(rc_dic2['Matricula'], rc_dic2['precio'], 1)
            Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t2)

            sumPrecio+=(float(rc_dic2['precio'])*int(c_obj_t2.get_dias()))

        Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)

    def test_viaje_gestionar_vehiculos1(self):

        lista = self.Viaje_t2.get_vehiculos()
        assert len(lista) == 2

    # def test_viaje_con_alojamientos_precio1(self):
    #
    #     precio = self.Viaje_t2.get_precio()
    #     assert precio == float(self.sumPrecio)



# ####Cuando se quitan vehiculos
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

        sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))
        Destinos_t3.add_destino("d001",v_obj_t3,None)

        rc_dic3=Rentalcars.Rentalcars().buscar_coche("1234ABC")
        if rc_dic3!="No encontrado":
            c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
            Destinos_t3.get_destino("d001").set_vehiculo(c_obj_t3)

            sumPrecio3+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))




    sc_dic3=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic3!="No encontrado":
        v_obj_t3=Flights.Flights(sc_dic3['ID'],sc_dic3['precio'])#id, precio

        sumPrecio3+=(float(sc_dic3['precio'])*int(Viajeros_t3.get_num_viatgers()))
        Destinos_t3.add_destino("d002",v_obj_t3,None)

        rc_dic3=Rentalcars.Rentalcars().buscar_coche("7351VEL")
        if rc_dic3!="No encontrado":
            c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
            Destinos_t3.get_destino("d002").set_vehiculo(c_obj_t3)

            sumPrecio3+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))

        Viaje_t3 = Viaje("v001", Viajeros_t3, Destinos_t3, Usuario_t3)


    Destinos_t3.get_destino("d001").remove_vehiculo();

    def test_viaje_gestionar_vehiculos2(self):

        lista = self.Viaje_t3.get_vehiculos()
        assert len(lista) == 1

    # def test_viaje_con_alojamientos_precio2(self):
    #
    #     precio = self.Viaje_t2.get_precio()
    #     assert precio == float(self.sumPrecio)
