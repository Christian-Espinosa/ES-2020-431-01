import Viatgers as Viatgers
from API import Hotels 
from API import Flights as Flights

from API import Rentalcars as Rentalcars
from API import Booking as Booking
from API import Cars as Cars
from API import Skyscanner as Skyscanner

class CalcularPrecio:
   def __init__(self, metodoPago, Pasajeros, hotel, coche, vuelo):
      self.metodoPago = metodoPago
      self.Pasajeros = Pasajeros
      self.Hotel = hotel
      self.Coche=coche
      self.Vuelo=vuelo
      self.precio=0

   def calc_precio(self):
      
      if self.Coche.ID is not None:
         rc=Rentalcars.Rentalcars()
         res=rc.buscar_coche(self.Coche.ID)
         if res!="No encontrado":
            self.precio+=(res*self.Coche.get_dias())

      if self.Hotel is not None:
         b=Booking.Booking()
         res=b.buscar_hotel(self.Hotel.ID)
         if res!="No encontrado":
            self.precio+=(res*self.Hotel.dias*self.Hotel.numHab)

      if self.Vuelo is not None:
         sk=Skyscanner.Skyscanner()
         res=sk.buscar_vuelo(self.Vuelo.ID)
         if res!="No encontrado":
            self.precio+=(res*self.Pasajeros.get_num_viatgers())
            
      return self.precio

      

        
      
