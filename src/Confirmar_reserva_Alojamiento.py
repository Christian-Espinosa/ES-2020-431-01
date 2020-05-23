import os
import os.path
from Viaje import Viaje
from Destino import Destino
from API.Airhopping.Booking import Booking

class Confirmar_reserva_Alojamiento:

    def __init__(self, user, nviatgers, alojamiento, viaje):
        
        self.user = user
        self.alojamiento = alojamiento
        self.viatgers = nviatgers
        self.viatge_reserva= viaje
        self.intentos=4
        
    def Confirmar_Alojamiento(self,user,alojamiento, nviatgers):
        
        if(self.intentos<=0):
            return False
        elif((self.viatge_reserva.get_alojamientos()!=alojamiento) or ( alojamiento == [])):
            self.intentos=self.intentos-1
            return False
        elif((self.viatge_reserva.get_user()!= user) or (user == [])):
            self.intentos=self.intentos-1
            return False
        elif((self.viatge_reserva.get_num_viatgers() != nviatgers) or (nviatgers == [])):
            self.intentos=self.intentos-1
            return False
        else:
            book = Booking()
            return(book.confirm_reserve(user,alojamiento))
