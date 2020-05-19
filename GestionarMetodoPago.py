import CalcularPrecio
from API.Airhopping import User
from API.Precio import Bank
class GestionarMetodoPago:
    
    def __init__(self, Pasajeros, Destinos):
        self.precio = CalcularPrecio(Pasajeros, Destinos).calc_precio()
        
    def Pagar(User, contra, metodo, importe):
            if Bank(User, contra).Pagar(self.precio, metodo) == True:
                print("Transacció correcta")
            else:
                print("Transacció incorrecta")
    