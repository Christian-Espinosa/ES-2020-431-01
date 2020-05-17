import CalcularPrecio
from API.AirHopping import User
class GestionarMetodoPago:
    
    def __init__(self, Pasajeros, Destinos):
        self.precio = CalcularPrecio(Pasajeros, Destinos).calc_precio()
        
    def Pagar(User:User, contra, metodo:str, importe:int):
            if Bank(User, contra).Pagar(self.precio, metodo):
                print("Transacció correcta")
            elif:
                print("Transacció incorrecta")
    