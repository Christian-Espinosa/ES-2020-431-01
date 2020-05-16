import Viatgers as Viatgers
import Destinos as Destinos
import CalcularPrecio as CalcularPrecio
import User as User

class Viaje:
    
    precio=0
    
    

    def __init__(self,id:str, Viatgers_Obj, Destinos_Obj):
        self.id=id
        self.precio=precio
        self.Viatgers_Obj=Viatgers_Obj
        self.Destinos_Obj=Destinos_Obj
        #self.precio=CalcularPrecio.CalcularPrecio().....
        

    def get_id(self)->str:
        return self.id

	def get_precio(self):
        return self.precio

	def get_viatgers(self):
		return self.Viatgers_Obj.get_viatgers()
		
	def get_destinos(self):
		return self.Destinos_Obj.get_lista_destinos()