import CalcularPrecio
from API.Airhopping import User
from API.Precio import Bank
class GestionarMetodoPago:
    
    def __init__(self, precio, Usuario, metodo):
        self.precio = precio
        self.usuario=Usuario
        self.metodo=metodo
        
    def Pagar(self):
            if Bank(self.usuario).Pagar(self.precio, self.metodo) == True:
                print("Transaccio correcta")
            else:
                print("Transaccio incorrecta")
    