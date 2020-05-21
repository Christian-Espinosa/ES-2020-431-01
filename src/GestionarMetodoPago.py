import CalcularPrecio
from API.Airhopping import User
from API.Precio.Bank import Bank
class GestionarMetodoPago:
    
    def __init__(self, precio, Usuario, metodo):
        self.precio = precio
        self.usuario=Usuario
        self.metodo=metodo
        
    def Pagar(self):
        return Bank().do_payment(self.usuario,self.metodo,self.precio)
            #if Bank(self.usuario).Pagar(self.precio, self.metodo) == True:
                #print("Transaccio correcta")
            #else:
                #print("Transaccio incorrecta")
    