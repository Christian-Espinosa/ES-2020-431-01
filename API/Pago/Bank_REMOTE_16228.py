from API.AirHopping import User as User
from API.AirHopping import User_ini as User_ini
from API.Pago import PaymentData as PaymentData


class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True