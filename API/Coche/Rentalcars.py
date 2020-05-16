import API.AirHopping.User as User
import API.AirHopping.User_ini as User_ini
import Cars


class Rentalcars():

    def __init__(self):
        pass

    def buscar_coche(self, matricula):
        f = open("API/Rentalcars.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            if id==matricula:
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
        return "Coche no encontrado"

    def confirm_reserve(self, user: User, cars: Cars) -> bool:
        return True