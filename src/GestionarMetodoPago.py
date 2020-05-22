import CalcularPrecio
import Viatgers
import Destinos
from API.Airhopping import User
from API.Precio.Bank import Bank

class GestionarMetodoPago:
    
    def __init__(self, precio, Viaje_Obj, metodo):
        self.done = False
        if 1<len(Viaje_Obj.Viatgers_Obj.get_viatgers()) and 1<Viaje_Obj.Destinos_Obj.get_num_destinos():
            if metodo == "MasterCard":
                self.done = True
                self.metodo = "MasterCard"
            elif metodo == "Visa":
                self.done = True
                self.metodo = "Visa"
            if self.done == True:
                self.viaje = Viaje_Obj
        
        
    def Pagar(self):
        if self.done:
            return Bank().Pagar()

