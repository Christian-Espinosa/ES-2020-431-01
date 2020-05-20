from API.Airhopping import User
from API.Airhopping import User_ini

class Bank:

    def __init__(self, user, contra,pay):
        self.user = user.DNI
        self.num_cuenta = pay.numero
        self.codigo_s = pay.codi_seg
        self.contra=contra
        
    def Pagar(self, importe, metodo):
        if metodo=="Visa":
            Visa(self.num_cuenta, importe).pagar()
            return True
        elif metodo=="MasterCard":
            MasterCard(self.num_cuenta, importe).pagar()
            return True
        return False