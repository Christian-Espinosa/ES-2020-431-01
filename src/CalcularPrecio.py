from Viatgers import Viatgers as Viatgers
from API.Airhopping import Hotels as Hotels
from API.Vuelos import Flights as Flights

from API.Coche import Rentalcars as Rentalcars
from API.Airhopping import Booking as Booking
from API.Coche import Cars as Cars
from API.Vuelos import Skyscanner as Skyscanner

class CalcularPrecio:
   def __init__(self, Pasajeros, Destinos):
      self.Pasajeros = Pasajeros
      self.destinos=Destinos
      self.precio=0

   def calc_precio(self):

      for d in self.destinos.get_lista_destinos():

         if d.get_vehiculo() is not None:
            rc=Rentalcars.Rentalcars()
            res=rc.buscar_coche(d.get_vehiculo().get_id())
            if res!="No encontrado":
               self.precio+=(float(res['precio'])*int(d.get_vehiculo().get_dias()))

         if d.get_hotel() is not None:
            b=Booking.Booking()
            res=b.buscar_hotel(d.get_hotel().ID)
            if res!="No encontrado":
               self.precio+=(float(res['precio'])*int(d.get_hotel().dias)*int(d.get_hotel().numHab))

         if d.get_vuelo() is not None:
            sk=Skyscanner.Skyscanner()
            res=sk.buscar_vuelo(d.get_vuelo().get_id())
            if res!="No encontrado":
               self.precio+=(float(res['precio'])*int(self.Pasajeros.get_num_viatgers()))



      return self.precio
