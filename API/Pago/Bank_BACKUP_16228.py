<<<<<<< HEAD
from API.AirHopping import User
from . import PaymentData
=======
from API.AirHopping import User as User
from API.AirHopping import User_ini as User_ini
from API.Pago import PaymentData as PaymentData
>>>>>>> a7a81cd24ac661a209051c7e35a128308208d383


class Bank:

    def __init__(self, user: User, contra):
        self.user = user.DNI
        self.contra = contra

    def do_payment(self, user: User, payment_data: PaymentData):
        if self.user == user.DNI:
            return True, payment_data.importe
        else:
            retrun False