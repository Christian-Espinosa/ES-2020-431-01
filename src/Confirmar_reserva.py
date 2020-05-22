# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:25:43 2020

@author: usuari
"""
import os
import os.path
from API.Airhopping import User
from Viaje import Viaje as Viaje
from Viatgers import Viatgers
from API.Vuelos import Skyscanner
from API.Vuelos import Flights
from API.Airhopping import Booking
from API.Airhopping import Hotels
from API.Coche import Rentalcars
from API.Coche import Cars

class Confirmar_reserva:
    ViatgeReserva=None
    def __init__(self,lista_avion, usuario,viatgers):
        self.lista_avion=lista_avion
        self.usuario=usuario
        self.viatgers= viatgers


    
    def GuardarViatge(self, ViatgeReserva):
        self.ViatgeReserva= ViatgeReserva

    def ConfirmacioReserva(self,llista_avions,user,nviatgers):
        #Problema con la inicialización y puede que viaje
        if((self.ViatgeReserva.get_vuelos()!=llista_avions) or ( llista_avions == [])):
            return False
        elif((self.ViatgeReserva.get_user()!= user) or (user == "Empty")):
            return False
        elif((self.ViatgeReserva.get_num_viatgers() != nviatgers) or (nviatgers== "Empty")):
            return False
        else:
            sk = Skyscanner.Skyscanner()
            bk = Booking.Booking()
            return (sk.confirm_reserve(user, llista_avions) and bk.confirm_reserve(user, llista_avions))
        
 
        
