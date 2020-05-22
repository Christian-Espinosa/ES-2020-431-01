from API.Vuelos import Flights as Fligths
from API.Airhopping import Hotels as Hotels


class Destino:

    def __init__(self,id_destino,vuelo,hotel):
        self.id_destino=id_destino
        self.vuelo=vuelo
        self.hotel=hotel
        #self.precioTotalPack=CalcularPrecio.CalcularPrecio("Visa", Viatgers_Obj,Destinos_Obj., )
        self.vehiculo=None

    
    def set_hotel(self, hotel):
        self.hotel=hotel
    def set_vehiculo(self, vehiculo):
        self.vehiculo=vehiculo

    def get_vuelo(self):
        return self.vuelo

    def get_id(self):
        return self.id_destino


    def get_hotel(self):
        return self.hotel

    def get_vehiculo(self):
        return self.vehiculo

    def remove_vehiculo(self):
        self.vehiculo=None
