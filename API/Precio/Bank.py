from API.AirHopping import User
from API.AirHopping import User_ini
from API.Pago import PaymentData as pay


class Bank:

    def __init__(self, user: User, contra):
        self.user = user.DNI
        self.num_cuenta = pay.num_cuenta
        self.codigo_s = pay.codigo_s
        
    def Pagar(self, importe, metodo):
        if metodo=="Visa":
            Visa(self.num_cuenta, importe).Pagar
            return True
        elif metodo=="MasterCard":
            MasterCard(self.num_cuenta, importe).Pagar
            return True
        return False