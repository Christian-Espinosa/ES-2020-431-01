from CalcularPrecio import CalcularPrecio
from GestionarMetodoPago import GestionarMetodoPago




class Viaje:


    def __init__(self,id_viaje, Viatgers_Obj, Destinos_Obj, User_Obj):
        self.id_viaje=id_viaje
        self.precio=0
        self.Viatgers_Obj=Viatgers_Obj
        self.Destinos_Obj=Destinos_Obj
        self.User_Obj=User_Obj

        cp=CalcularPrecio(Viatgers_Obj,Destinos_Obj)
        self.precio=cp.calc_precio()

    def get_id_viaje(self):
        return self.id_viaje

    def get_user(self):
        return self.User_Obj

    def get_precio(self):
        cp=CalcularPrecio(self.Viatgers_Obj,self.Destinos_Obj)
        self.precio=cp.calc_precio()
        return self.precio

    def get_viatgers(self):
        return self.Viatgers_Obj.get_viatgers()

    def get_num_viatgers(self):
        return self.Viatgers_Obj.get_num_viatgers()

    def get_destinos(self):
        return self.Destinos_Obj.get_lista_destinos()

    def get_vuelos(self):
        list_vuelos_t=[]
        if len(self.Destinos_Obj.get_lista_destinos()) > 0:
            for d in self.Destinos_Obj.get_lista_destinos():
                list_vuelos_t.append(d.get_vuelo())

        return list_vuelos_t

    def remove_destino(self, id):
        if self.Destinos_Obj.num_destinos > 0:
            self.Destinos_Obj.remove_destino(id)

    def pagar(self,metodo):
        res=GestionarMetodoPago(self.precio, self.User_Obj, metodo)
        res=res.Pagar()
        return res

    def remove_alojamiento(self, id_dest):
        if len(self.Destinos_Obj.get_lista_destinos()) > 0:
            for d in self.Destinos_Obj.get_lista_destinos():
                if d.get_id()==id_dest:
                    d.hotel=None
    
    def remove_car(self, id_car):
        if len(self.Destinos_Obj.get_lista_destinos()) > 0:
            for d in self.Destinos_Obj.get_lista_destinos():
                if d.get_id()==id_dest
                    d.vehiculo=None
