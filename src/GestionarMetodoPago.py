import CalcularPrecio
import Viatgers
import Destinos
from API.Airhopping import User
from API.Precio.Bank import Bank

class GestionarMetodoPago:
    
    def gestor_de_caracteristicas(self):
        if 1<= self.viaje.get_num_viatgers() and 1<=self.viaje.Destinos_Obj.get_num_destinos():
            if self.metodo == "MasterCard" or self.metodo == "Visa":
                self.done = True
                self.usuario = self.viaje.User_Obj
        else:
            print("pedo")
            self.done = False
            
    def __init__(self, precio, Viaje_Obj, metodo):
        self.done = False
        self.metodo = metodo
        self.pagar_count = 0
        self.viaje = Viaje_Obj
        self.importe = precio
        self.gestor_de_caracteristicas()

    
        
    def Pagar(self):
        #esta funcion pagar tiene en cuenta que usuario la ha ejecutado!
        print("Pagar")
        self.gestor_de_caracteristicas()
        if self.pagar_count < 3:
            if self.done:
                return Bank().do_payment(self.usuario, self.metodo, self.importe)
            else:
                #error
                self.pagar_count += 1
        else:
            return False

