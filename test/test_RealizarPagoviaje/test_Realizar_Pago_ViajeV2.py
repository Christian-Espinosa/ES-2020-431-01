# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:38:55 2020

@author: usuari
"""


import os
import sys
import unittest
from unittest import mock


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)




#from src.GestionarMetodoPago import GestionarMetodoPago 
#from src.Viaje import Viaje
from Viatgers import Viatgers as Viatgers
from API.Airhopping import User as User
from Destinos import Destinos as Destinos
from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights as Flights
from API.Airhopping import Booking as Booking
from API.Airhopping import Hotels as Hotels
from API.Coche import Rentalcars as Rentalcars
from API.Coche import Cars as Cars
from Viaje import Viaje as Viaje


"""
-Dado un viaje con múltiples destinos y más de un viajero,cuando se produce un error al realizar el pago, se reporta 
que la acción no se ha podido realizar
"""


class TestGestiondepagoV2(unittest.TestCase):

    @mock.patch('Viaje.Viaje')
    def test_realizarPagoV2(self, mock_realizarPago):
        id_viaje="9981728"
        

        lista_destinosTemp=[]


        Viatgers_Obj_temp = Viatgers()
       
        nombre_t = "Juan Antonio"
        apellidos_t = "Llop"
        dni_t = "172882F"
        edad = "30"
        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)

        nombre_t = "Marcel"
        apellidos_t = "Gibralto"
        dni_t = "82819M"
        edad = "60"

        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)

        nombre_t = "Agustin"
        apellidos_t = "Copon"
        dni_t = "817201J"
        edad = "20"

        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)



        #Usuario (User) ID ONLY

        Usuario="981293K"

        User_Obj_temp = User.User()
        Usuario_Obj_temp = User_Obj_temp.getDatosUser(Usuario)


        #Destino


        Destinos_Obj_temp = Destinos()
        

        id_destino_t="D_98293432"
        sc_dic=Skyscanner.Skyscanner().buscar_vuelo("F_78293")
        v_obj_t=Flights.Flights(sc_dic[0],sc_dic[2])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("H_827382")
        h_obj_t=Hotels.Hotels("5", bk_dic[0], "54", "2", bk_dic[1])
        h_obj_t.setPrecio(bk_dic[2])#precio

        Destinos_Obj_temp.add_destino(id_destino_t,v_obj_t,h_obj_t)

        id_coche_t = "C_283782"
        dias_coche_t = "2"

        car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

        precio_coche_t = car_dic[2]

        car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

        if Destinos_Obj_temp.get_destino(id_destino_t) != None:
            Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)


         #Destino2


        Destinos_Obj_temp = Destinos()
        

        id_destino_t="D_273832"
        sc_dic=Skyscanner.Skyscanner().buscar_vuelo("F_27382")
        v_obj_t=Flights.Flights(sc_dic[0],sc_dic[2])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("H_8391822")
        h_obj_t=Hotels.Hotels("3", bk_dic[0], "10", "2", bk_dic[1])
        h_obj_t.setPrecio(bk_dic[2])#precio

        Destinos_Obj_temp.add_destino(id_destino_t,v_obj_t,h_obj_t)

        id_coche_t = "C_283292"
        dias_coche_t = "2"

        car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

        precio_coche_t = car_dic[2]

        car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

        if Destinos_Obj_temp.get_destino(id_destino_t) != None:
            Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)
            

        mock_realizarPago(id_viaje,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp).pagar.return_value = False
        self.assertFalse(mock_realizarPago(id_viaje,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp).pagar())
        

        

