# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:25:43 2020

@author: usuari
"""

#from API.AirHopping import Booking as Booking 
#Falla enviar el confirm
from API.Vuelos import Skyscanner as Skyscanner

class Confirmar_Reserva:
    def __init__(self,lista_avion, usuario):
        self.lista_avion=lista_avion
        self.usuario=usuario
        
    
    def ConfirmacioReserva(self,llista_avions,user):
        self.llista = llista_avions
        self.usuari=user
        sk=Skyscanner.Skyscanner()
        return sk.confirm_reserve(user, llista_avions)
        
 
        
