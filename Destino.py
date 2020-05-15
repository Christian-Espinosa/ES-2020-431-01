class Destino:
    
    vuelo=""
    precioTotalPack=0
    hotel=""
    vehiculo=""
    id=""

    def __init__(self,id,vuelo,hotel,precio):
	    self.id=id
        self.vuelo=vuelo
        self.hotel=hotel
        self.precioTotalPack=precio

	def set_vehiculo(self, vehiculo):
		self.vehiculo=vehiculo
		
    def get_vuelo(self):
        return self.vuelo
        
    def get_id(self):
        return self.id
        
    def get_precioTotalPack(self):
        return self.precioTotalPack
        
    def get_hotel(self):
	    return self.hotel
	    
	def get_vehiculo(self):
	    return self.vehiculo
