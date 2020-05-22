from API.Coche import Rentalcars as Rentalcars

class Cars:

    id=""
    precio=0
    dias=0

    def __init__(self,id, precio, dias):
        self.id=id
        self.precio=precio
        self.dias=dias
        self.num_conexions=3

    def get_id(self):
        return self.id

    def get_precio(self):
        return self.precio
        
    def get_dias(self):
        return self.dias

    def confirmar(self, User, cars):
        if(self.num_conexions>0):
            self.num_conexions-=1
            rc=Rentalcars.Rentalcars()
            return rc.confirm_reserve(User, cars)
        else:
            return False
