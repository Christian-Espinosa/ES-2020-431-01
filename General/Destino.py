import API.Vuelo as Fligths
import API.Hotel as Hotels


class Destino:

    def __init__(self,id_destino,vuelo,hotel):
        self.id_destino=id_destino
        self.vuelo=vuelo
        self.hotel=hotel
        #self.precioTotalPack=llamar a clacular precio...
        self.vehiculo="None Car"

    def set_vehiculo(self, vehiculo):
        self.vehiculo=vehiculo
        
    def get_vuelo(self):
        return self.vuelo
        
    def get_id(self):
        return self.id_destino
        
    def get_precioTotalPack(self):
        return self.precioTotalPack
        
    def get_hotel(self):
        return self.hotel
        
    def get_vehiculo(self):
        return self.vehiculo
