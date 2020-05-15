import User as User
import Hotels as Hotels



class Booking():

    def __init__(self):
        pass

    def precio_hotel(self, ID):
        self.lista_Hotels=[]
        f = open("API/Booking.txt")
        linea = f.readline()
        while linea != "":
            nombre=linea
            linea = f.readline()
            DNI=linea
            linea = f.readline()
            
            calle=linea
            linea = f.readline()

            tel=linea

            linea = f.readline()
            email=linea

            self.lista_Hotels.append(Hotels.Hotels(nombre,DNI,calle,tel,email))
            linea = f.readline()

            


        f.close()

    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        return True