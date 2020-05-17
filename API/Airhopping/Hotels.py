class Hotels:

    def __init__(self, dias, ID, numHab, numHostes, nombre):
        self.dias=dias
        self.ID=ID
        self.precio=0
        self.numHab=numHab
        self.numHostes=numHostes
        self.nombre=nombre
        
    def setPrecio(self, precio):
        self.precio=precio
