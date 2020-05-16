from General.CalcularPrecio import CalcularPrecio as CalcularPrecio
from General.GestionarMetodoPago import GestionarMetodoPago as GestionarMetodoPago


class Viaje:
    

    def __init__(self,id_viaje, Viatgers_Obj, Destinos_Obj, id_user):
        self.id_viaje=id_viaje
        self.precio=0
        self.Viatgers_Obj=Viatgers_Obj
        self.Destinos_Obj=Destinos_Obj
        self.id_user=id_user
        #self.precio=CalcularPrecio.CalcularPrecio().....
        

    def get_id_viaje(self):
        return self.id_viaje
    
    def get_id_user(self):
        return self.id_user

    def get_precio(self):
        return self.precio
    
    def get_viatgers(self):
        return self.Viatgers_Obj.get_viatgers()
    
    def get_destinos(self):
        return self.Destinos_Obj.get_lista_destinos()
    
    def pagar(self,metodo):
        return GestionarMetodoPago(self.id_viaje, self.id_user, metodo)