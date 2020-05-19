from API.Airhopping import User
from API.Airhopping import User_ini
from API.Precio import PaymentData as pay


class Bank:

    def __init__(self, user, contra):
        self.user = user.DNI
        self.num_cuenta = pay.num_cuenta
        self.codigo_s = pay.codigo_s
        
    def Pagar(self, importe, metodo):
        if metodo=="Visa":
            Visa(self.num_cuenta, importe).pagar()
            return True
        elif metodo=="MasterCard":
            MasterCard(self.num_cuenta, importe).pagar()
            return True
        return False