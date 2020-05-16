import API.Flights as Fligths
import API.Hotels as Hotels

class Destino:

    def __init__(self,id:str,vuelo:Fligths,hotel:Hotels,precio:float):
        self.id=id
        self.vuelo=vuelo
        self.hotel=hotel
        self.precioTotalPack=precio
        self.vehiculo=""

    def set_vehiculo(self, vehiculo):
        self.vehiculo=vehiculo
        
    def get_vuelo(self):
        return self.vuelo
        
    def get_id(self):
        return self.id
        
    def get_precioTotalPack(self):
        return self.precioTotalPack
        
    def get_hotel(self):
        return self.hotel
        
    def get_vehiculo(self):
        return self.vehiculo
