from API.AirHopping import User_ini as User_ini
from API.AirHopping import User as User
from API.Vuelo import Flights as Flights

class Skyscanner():

    def __init__(self):
        pass
    def buscar_vuelo(self, ID):
        self.lista_Vuelos=[]
        f = open("API/Skyscanner.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            if id==ID:
                linea = f.readline()
                nombre=linea
                linea = f.readline()
                precio=linea
                f.close()
                VueloDict = {
                    "ID": id,
                    "Nombre": nombre,
                    "precio": precio,
                }
                return VueloDict
               
            linea = f.readline()

            
        f.close()
        return  "No encontrado"

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True