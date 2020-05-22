import CalcularPrecio
import Viatgers
import Destinos
from API.Airhopping import User
from API.Precio.Bank import Bank

class GestionarMetodoPago:
    
    def __init__(self, precio, Viaje_Obj, metodo):
        self.done = False
        self.metodo = None
        if 1<len(Viaje_Obj.Viatgers_Obj.get_viatgers()) and 1<Viaje_Obj.Destinos_Obj.get_num_destinos():
            if metodo == "MasterCard":
                self.done = True
                self.metodo = "MasterCard"
            elif metodo == "Visa":
                self.done = True
                self.metodo = "Visa"
            if self.done == True:
                self.viaje = Viaje_Obj
                self.importe = precio
                self.usuario = Viaje_Obj.User_Obj
        
        
    def Pagar(self):
        if self.done:
            return Bank().do_payment(self.usuario, self.metodo, self.importe)

