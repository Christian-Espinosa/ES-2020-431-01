from API.AirHopping import User
from API.AirHopping import User_ini
from API.Pago import PaymentData


class Bank:

    def __init__(self, user: User, contra):
        self.user = user.DNI
        self.contra = contra

    def do_payment(self, user: User, payment_data: PaymentData):
        if self.user == user.DNI:
            return True, payment_data.importe
        else:
            return False