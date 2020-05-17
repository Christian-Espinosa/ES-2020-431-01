import CalcularPrecio
from API.AirHopping import User
class GestionarMetodoPago:
    
    def __init__(self, Pasajeros, Destinos):
        self.precio = CalcularPrecio(Pasajeros, Destinos).calc_precio()
        
    def Pagar(User:User, contra, metodo, importe):
            b = Bank(User, contra).Pagar
            if b:
                print("Transacció correcta")
            elif:
                print("Transacció incorrecta")
    