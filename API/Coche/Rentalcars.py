from API.AirHopping import User as User
from API.AirHopping import User_ini as User_ini
from API.Coche import Cars as Cars






class Rentalcars:

    def __init__(self):
        pass
    def buscar_coche(self,ID:str):
        f = open("API/Rentalcars.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            if id==ID:
                linea = f.readline()
                nombre=linea
                linea = f.readline()
                precio=linea
                f.close()
                CocheDict = {
                    "Matricula": id,
                    "Nombre": nombre,
                    "precio": precio,
                }
                return CocheDict
               
            linea = f.readline()

            
        f.close()
        return  "No encontrado"

    def confirm_reserve(self, user: User, cars: Cars) -> bool:
        return True