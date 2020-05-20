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

"""
-Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se
realiza correctamente, se reporta que la acción se ha realizado correctamente

"""


class TestGestiondepago(unittest.TestCase):


    def test_realizarPago(self):
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
        


        sc_dic=Skyscanner.Skyscanner().buscar_vuelo("F_78293")
        v_obj_t=Flights.Flights(sc_dic[0],sc_dic[2])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("H_827382")
        h_obj_t=Hotels.Hotels("5", bk_dic[0], "54", "2", bk_dic[1])
        h_obj_t.setPrecio(bk_dic[2])#precio

        Destinos_Obj_temp.add_destino("D_98293432",v_obj_t,h_obj_t)

        id_coche_t = "C_283782"
        dias_coche_t = "2"

        car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

        precio_coche_t = car_dic[2]

        car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

        if Destinos_Obj_temp.get_destino(id_destino_t) != None:
            Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)

        lista_Viajes.append(Viaje(id_viaje_t,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp))



