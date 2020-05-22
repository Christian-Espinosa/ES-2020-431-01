# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:16:41 2020

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


from unittest import mock

from API.Coche import Rentalcars as Rentalcars
from API.Coche import Cars as Cars
from API.Airhopping import User as User

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

class Test_mock_reserva_vehiculo(unittest.TestCase):






    @mock.patch('API.Coche.Rentalcars')
    def test_confirm_reserve(self, mock_reserva_vehiculo):
        sumPrecio=0

        Destinos_t2 = Destinos()
        Viajeros_t2 = Viatgers()

        User_t2 = User.User()
        Usuario_t2 = User_t2.getDatosUser("787372-P")
        c_obj_t3=0

        Viajeros_t2.add_viatger("Alex","Alaminos","12345678P","23")
        Viajeros_t2.add_viatger("Anna","Dot","98765432P","20")

        sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f001")
        if sc_dic2!="No encontrado":
            v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

            bk_dic2=Booking.Booking().buscar_hotel("h001")
            if bk_dic2!="No encontrado":
                h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                #Hotel + Vuelo
                sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)
                rc_dic3=Rentalcars.Rentalcars().buscar_coche("C_302165")
                if rc_dic3!="No encontrado":
                    c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                    Destinos_t2.get_destino("d001").set_vehiculo(c_obj_t3)

                    sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))


        sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
        if sc_dic2!="No encontrado":
            v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

            bk_dic2=Booking.Booking().buscar_hotel("h002")
            if bk_dic2!="No encontrado":
                h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                #Hotel + Vuelo
                sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

                rc_dic3=Rentalcars.Rentalcars().buscar_coche("1234ABC")
                if rc_dic3!="No encontrado":
                    c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                    Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t3)

                    sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))

                    Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)

        ##sin errores
        self.assertTrue(c_obj_t3.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))
       


class Test_mock_reserva_vehiculo2(unittest.TestCase):
        @mock.patch('API.Coche.Rentalcars')
        def test_confirm_reserve2(self, mock_reserva_vehiculo):
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

                bk_dic2=Booking.Booking().buscar_hotel("h001")
                if bk_dic2!="No encontrado":
                    h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                    h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                    #Hotel + Vuelo
                    sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                    sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                    Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)
                    rc_dic3=Rentalcars.Rentalcars().buscar_coche("C_302165")
                    if rc_dic3!="No encontrado":
                        c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                        Destinos_t2.get_destino("d001").set_vehiculo(c_obj_t3)

                        sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))


            sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
            if sc_dic2!="No encontrado":
                v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

                bk_dic2=Booking.Booking().buscar_hotel("h002")
                if bk_dic2!="No encontrado":
                    h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                    h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                    #Hotel + Vuelo
                    sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                    sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                    Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

                    rc_dic3=Rentalcars.Rentalcars().buscar_coche("1234ABC")
                    if rc_dic3!="No encontrado":
                        c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                        Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t3)

                        sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))

                        Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)


            ##con errores
            mock_reserva_vehiculo.confirmar.return_value = False
            self.assertFalse(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))
