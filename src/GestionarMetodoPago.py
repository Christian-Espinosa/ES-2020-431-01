import CalcularPrecio
import Viatgers
import Destinos
from API.Airhopping import User
from API.Precio.Bank import Bank
from API.Precio.PaymentData import PaymentData

class GestionarMetodoPago:
    
    def gestor_de_caracteristicas(self):
        if 1<= self.viaje.get_num_viatgers() and 1<=self.viaje.Destinos_Obj.get_num_destinos():
            if self.metodo == "MasterCard" or self.metodo == "Visa":
                self.done = True
                self.usuario = self.viaje.User_Obj
            else:
                self.done = False
        else:
            self.done = False
            
    def __init__(self, precio, Viaje_Obj, metodo):
        self.done = False
        self.metodo = metodo
        self.pagar_count = 0
        self.viaje = Viaje_Obj
        self.importe = precio
        self.gestor_de_caracteristicas()

    def verifica_credenciales(self, titular, cuenta, codigo_seg):
        p = PaymentData(titular)
        dic = p.leer_datos()
        
        if isinstance(dic,dict):
            if dic["Numero"] == cuenta and dic["Codigo seguridad"] == codigo_seg:
                self.done = True
            else:
                self.done = False
        else:
            self.done = False
        
    def Pagar(self):
        #versiones V2 y V4
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
        
    def Pagar_credenciales(self, titular, cuenta, codigo_seg):
        #versiones V5
        #esta funcion pagar tiene en cuenta que usuario la ha ejecutado!
        self.gestor_de_caracteristicas()
        self.verifica_credenciales(titular, cuenta, codigo_seg)
        if self.pagar_count < 3:
            if self.done:
                return Bank().do_payment(self.usuario, self.metodo, self.importe)
            else:
                #error
                self.pagar_count += 1
                return False
        else:
            return False

