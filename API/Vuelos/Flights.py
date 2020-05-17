class Flights:

    id=""
    precio=0

    def __init__(self,id, precio):
        self.id=id
        self.precio=precio

    def get_id(self):
        return self.id

    def get_precio(self):
        return self.precio
