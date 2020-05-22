import CalcularPrecio
import Viatgers
import Destinos
from API.Airhopping import User
from API.Precio.Bank import Bank

class GestionarMetodoPago:
    
    def gestor_de_caracteristicas(self):
        if 1<=len(self.viaje.Viatgers_Obj.get_viatgers()) and 1<=self.viaje.Destinos_Obj.get_num_destinos():
            if self.metodo == "MasterCard":
                self.done = True
            elif self.metodo == "Visa":
                self.done = True
                
            if self.done == True:
                self.usuario = self.viaje.User_Obj
        else:
            self.done = False
            
    def __init__(self, precio, Viaje_Obj, metodo):
        self.done = False
        self.metodo = metodo
        self.pagar_count = 0
        self.viaje = Viaje_Obj
        self.importe = precio
        self.gestor_de_caracteristicas()

    
                
    def set_viatje(self, Viaje_Obj):
        self.viaje = Viatgers_Obj

        
    def Pagar(self):
        #esta funcion pagar tiene en cuenta que usuario la ha ejecutado!
        self.gestor_de_caracteristicas()
        if self.pagar_count < 3:
            if self.done:
                return Bank().do_payment(self.usuario, self.metodo, self.importe)
            else:
                #error
                self.pagar_count += 1
        else:
            return False

