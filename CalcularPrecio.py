import Viatgers as Viatgers
from API import Hotels 
from API import Flights as Flights

from API import Rentalcars as Rentalcars
from API import Booking as Booking
from API import Cars as Cars
from API import Skyscanner as Skyscanner

class CalcularPrecio:
   def __init__(self, Pasajeros, Destinos):
      self.Pasajeros = Pasajeros
      self.destinos=Destinos
      self.precio=0

   def calc_precio(self):
      
      for d in self.destinos.get_lista_destinos(): 
         if d.get_vehiculo() is not None:
            rc=Rentalcars.Rentalcars()
            res=rc.buscar_coche(d.get_vehiculo().ID)
            if res!="No encontrado":
               self.precio+=(res['precio']*d.get_vehiculo().ID.get_dias())

         if g.get_hotel() is not None:
            b=Booking.Booking()
            res=b.buscar_hotel(d.get_hotel().ID)
            if res!="No encontrado":
               self.precio+=(res['precio']*d.get_hotel().dias*d.get_hotel().numHab)

         if d.get_vuelo() is not None:
            sk=Skyscanner.Skyscanner()
            res=sk.buscar_vuelo(d.get_vuelo().ID)
            if res!="No encontrado":
               self.precio+=(res['precio']*self.Pasajeros.get_num_viatgers())
            
      return self.precio

      

        
      
