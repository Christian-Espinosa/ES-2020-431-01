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
Dado un viaje con más de un viajero, cuando se añaden alojamientos, el precio
del viaje es el esperado

Dado un viaje con más de un viajero, cuando se quitan alojamientos, el precio
del viaje es el esperado

"""


class test_Gestionar_Metodo_de_Pago(unittest.TestCase):

    Destinos_t = Destinos()
    Viajeros_t = Viatgers()

    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")

    Viajeros_t.add_viatger("Alex","Alaminos","12345678P","23")
    Viajeros_t.add_viatger("Anna","Dot","98765432P","20")
    
    #Destinos
    sc_dic=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic!="No encontrado":
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("h001")
        if bk_dic!="No encontrado":
            h_obj_t=Hotels.Hotels(2, bk_dic['ID'], 1, 1, bk_dic['Nombre'])
            h_obj_t.setPrecio(bk_dic['precio'])#precio
            
            Destinos_t.add_destino("d001",v_obj_t,h_obj_t)
            
            
    
    sc_dic=Skyscanner.Skyscanner().buscar_vuelo("f002")
    if sc_dic!="No encontrado":
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("h001")
        if bk_dic!="No encontrado":
            h_obj_t=Hotels.Hotels(2, bk_dic['ID'], 1, 1, bk_dic['Nombre'])
            h_obj_t.setPrecio(bk_dic['precio'])#precio
            
            Destinos_t.add_destino("d001",v_obj_t,h_obj_t)
            
            
            
            Destinos_t.add_destino("d002",v_obj_t,h_obj_t)
    
    Viaje_t = Viaje.Viaje(0, Viajeros_t, Destinos_t, Usuario_t)
    
    metodo = "Visa"
    GestionarMetodoPago(Viaje_t, metodo)
    
    

    def test_Gestionar_Metodo_Visa(self):
        
        x = GestionarMetodoPago(Viaje_t, metodo)
        assert x.done == True and x.metodo == "Visa"
    

    
    

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

    obj_viaje=Viaje(id_viaje,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp)
    res=obj_viaje.pagar("Visa")
    
    def test_Gestionar_Metodo_Visa_sin_personas(self):
        
        
        

    def test_viaje_con_alojamientos_precio_eliminar(self):

        precio = self.Viaje_t3.get_precio()
        assert precio == float(self.sumPrecio3)
