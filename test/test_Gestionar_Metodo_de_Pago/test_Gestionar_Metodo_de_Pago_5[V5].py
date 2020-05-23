import os
import sys
import unittest
import copy

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)


from Viaje import Viaje as Viaje
from Viatgers import Viatgers
from Destinos import Destinos

from API.Airhopping import User as User
from API.Airhopping import Booking as Booking
from API.Airhopping import Hotels as Hotels

from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights as Flights

from GestionarMetodoPago import GestionarMetodoPago
from CalcularPrecio import CalcularPrecio




class test_Gestionar_Metodo_de_Pago_Visa(unittest.TestCase):

    #Creamos destinos, viaje, viajeros
    Destinos_t = Destinos()
    Viajeros_t = Viatgers()
    
    #Usuario
    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")
    
    #Añadimos dos viajeros
    Viajeros_t.add_viatger("Alex","Alaminos","12345678P","23")
    
    #Destinos
    #Añadimos dos destinos
    sc_dic=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic!="No encontrado":
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("h001")
        if bk_dic!="No encontrado":
            h_obj_t=Hotels.Hotels(2, bk_dic['ID'], 1, 1, bk_dic['Nombre'])
            h_obj_t.setPrecio(bk_dic['precio'])#precio
            
            Destinos_t.add_destino("d001",v_obj_t,h_obj_t)
            
           
    
    
    Viaje_t = Viaje(0, Viajeros_t, Destinos_t, Usuario_t)
    
    metodo = "Visa"
    
    Viaje_t3 = copy.copy(Viaje_t)
    Viaje_t2 = copy.copy(Viaje_t)
    
    def test_Gestionar_Metodo_Visa_SinDestino(self):
        
        self.Viaje_t2.remove_destino("d001")
        x = GestionarMetodoPago(self.Viaje_t2.get_precio(), self.Viaje_t2, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        res = x.Pagar()
        assert x.done == False and x.pagar_count == 3
        assert not res
        res = x.Pagar()
        assert not res
    
    def test_Gestionar_Metodo_Visa_SinViajero(self):
        
        self.Viaje_t3.Viatgers_Obj.remove_viatger("Alex")
        x = GestionarMetodoPago(self.Viaje_t3.get_precio(), self.Viaje_t3, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        res = x.Pagar()
        assert x.done == False and x.pagar_count == 3
        assert not res
        res = x.Pagar()
        assert not res
    
    def test_Gestionar_Metodo_Visa_SinViajero_SALVADO(self):
        

        x = GestionarMetodoPago(self.Viaje_t.get_precio(), self.Viaje_t, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        x.viaje.Viatgers_Obj.add_viatger("Christian","Espinosa","11111111P","22")
        x.viaje.Destinos_Obj.add_destino("d001", self.v_obj_t, self.h_obj_t)
        
        res = x.Pagar()
        assert res
        assert x.done == True and x.pagar_count == 2
    
        

class test_Gestionar_Metodo_de_Pago_MasterCard(unittest.TestCase):

        
    #Creamos destinos, viaje, viajeros
    Destinos_t = Destinos()
    Viajeros_t = Viatgers()
    
    #Usuario
    User_t = User.User()
    Usuario_t = User_t.getDatosUser("787372-P")
    
    #Añadimos dos viajeros
    Viajeros_t.add_viatger("Alex","Alaminos","12345678P","23")
    
    #Destinos
    #Añadimos dos destinos
    sc_dic=Skyscanner.Skyscanner().buscar_vuelo("f001")
    if sc_dic!="No encontrado":
        v_obj_t=Flights.Flights(sc_dic['ID'],sc_dic['precio'])#id, precio

        bk_dic=Booking.Booking().buscar_hotel("h001")
        if bk_dic!="No encontrado":
            h_obj_t=Hotels.Hotels(2, bk_dic['ID'], 1, 1, bk_dic['Nombre'])
            h_obj_t.setPrecio(bk_dic['precio'])#precio
            
            Destinos_t.add_destino("d001",v_obj_t,h_obj_t)
            
            
    Viaje_t = Viaje(0, Viajeros_t, Destinos_t, Usuario_t)
    
    #Definimos metodo de pago
    metodo = "MasterCard"
    
    Viaje_t2 = copy.copy(Viaje_t)
    Viaje_t3 = copy.copy(Viaje_t)
    
    def test_Gestionar_Metodo_MasterCard_SinDestino(self):
        
        x.viaje.Viatgers_Obj.add_viatger("Christian","Espinosa","11111111P","22")
        x.viaje.Destinos_Obj.add_destino("d001", self.v_obj_t, self.h_obj_t)
        x = GestionarMetodoPago(self.Viaje_t2.get_precio(), self.Viaje_t2, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        res = x.Pagar()
        assert x.done == False and x.pagar_count == 3
        assert not res
        res = x.Pagar()
        assert not res
    
    def test_Gestionar_Metodo_MasterCard_SinViajero(self):
        
        self.Viaje_t3.Viatgers_Obj.remove_viatger("Alex")
        x = GestionarMetodoPago(self.Viaje_t3.get_precio(), self.Viaje_t3, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        res = x.Pagar()
        assert x.done == False and x.pagar_count == 3
        assert not res
        res = x.Pagar()
        assert not res
        
    def test_Gestionar_Metodo_MasterCard_SinViajero_SALVADO(self):
        

        x = GestionarMetodoPago(self.Viaje_t.get_precio(), self.Viaje_t, self.metodo)
        assert x.done == False and x.pagar_count == 0
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 1
        res = x.Pagar()
        assert not res
        assert x.done == False and x.pagar_count == 2
        x.viaje.Viatgers_Obj.add_viatger("Christian","Espinosa","11111111P","22")
        x.viaje.Destinos_Obj.add_destino("d001", self.v_obj_t, self.h_obj_t)
        
        res = x.Pagar()
        assert res
        assert x.done == True and x.pagar_count == 2
        
        
        