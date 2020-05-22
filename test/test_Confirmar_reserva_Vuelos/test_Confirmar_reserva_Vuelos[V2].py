# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:15:20 2020

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

from Confirmar_reserva_Vuelos import Confirmar_reserva_Vuelos
from API.Airhopping import User
from Destinos import Destinos
from Viatgers import Viatgers
from Viaje import Viaje as Viaje
from API.Airhopping import Booking
from API.Airhopping import Hotels
from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights
from API.Coche import Rentalcars
from API.Coche import Cars

##comando para ejecutar este test unicamente (Hay que estar en el directorio raiz ES-2020-431-01!!!! ) => pytest test/test_Confirmar_reserva_Vuelos
"""
-Dado un viaje con múltiples destinos y más de un viajero, cuando se produce error al confirmar los vuelos, 
se reporta que la acción no se ha podido realizar

"""


class TestConfirmar(unittest.TestCase):
    def test_confirmar_reserva_vuelos(self):
        #Creation of fictional travelers and travel id
        id_viaje="5467890"

        Viatgers_Obj_temp = Viatgers()
        
        
        nombre_t = "Elvis"
        apellidos_t = "Tek"
        dni_t = "165012A"
        edad = "28"
        
        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)

        nombre_t = "Juan"
        apellidos_t = "Vargas"
        dni_t = "456123H"
        edad = "18"

        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)

        nombre_t = "Fausto"
        apellidos_t = "Cristello"
        dni_t = "994751L"
        edad = "40"

        Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)

        #Creation of a fiction user

        Usuario="845612X"

        User_Obj_temp = User.User()
        Usuario_Obj_temp = User_Obj_temp.getDatosUser(Usuario)

        #Creation of fictional first destiny

        Destinos_Obj_temp = Destinos()
     
        id_destino_t="D_78945612"
        sc_dic=Skyscanner.Skyscanner().buscar_vuelo("F_45628")
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id=0, precio=2

        bk_dic=Booking.Booking().buscar_hotel("H_159753")
        h_obj_t=Hotels.Hotels("4", bk_dic['ID'], "60", "6", bk_dic['Nombre'])#Nombre=1
        h_obj_t.setPrecio(bk_dic['precio'])#precio

        Destinos_Obj_temp.add_destino(id_destino_t,v_obj_t,h_obj_t)
        #Vuelos -> Skyscanner
        #RentalCars -> Coches
        # Booking -> Hoteles
        id_coche_t = "C_302165"
        dias_coche_t = "6"
        
        #Creation of fictional car
        
        car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

        precio_coche_t = car_dic['precio']

        car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

        if Destinos_Obj_temp.get_destino(id_destino_t) != None:
            Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)


         


        id_destino_t="D_78945613"
        sc_dic=Skyscanner.Skyscanner().buscar_vuelo("F_45629")
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("H_159754")
        h_obj_t=Hotels.Hotels("4", bk_dic['ID'], "60", "2", bk_dic['Nombre'])
        h_obj_t.setPrecio(bk_dic['precio'])#precio

        Destinos_Obj_temp.add_destino(id_destino_t,v_obj_t,h_obj_t)
        #Creation of fictional car
        id_coche_t = "C_302166"
        dias_coche_t = "2"

        car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

        precio_coche_t = car_dic['precio']

        car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

        if Destinos_Obj_temp.get_destino(id_destino_t) != None:
            Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)
        
        obj_viaje=Viaje(id_viaje,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp)
        
        #init
        Reserva_Obj_temp= Confirmar_reserva_Vuelos(obj_viaje.get_vuelos(),obj_viaje.get_user(),obj_viaje.get_num_viatgers())
        
        Reserva_Obj_temp.GuardarViatge(obj_viaje)
        
        #No valid Vuelos

         
        res = Reserva_Obj_temp.ConfirmacioReserva("Empty",obj_viaje.get_user(),obj_viaje.get_num_viatgers())
        
        assert res == False

        #No valid User
        
        res = Reserva_Obj_temp.ConfirmacioReserva(obj_viaje.get_vuelos(),"Empty",obj_viaje.get_num_viatgers())
        
        assert res == False

        #No valid Nº Viatgers

        res = Reserva_Obj_temp.ConfirmacioReserva(obj_viaje.get_vuelos(),obj_viaje.get_user(),"Empty")
        
        assert res == False
