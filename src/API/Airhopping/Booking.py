#import User_ini as User_ini
#import User as User
#import Hotels as Hotels



class Booking:

    def __init__(self):
        pass
    def buscar_hotel(self, ID):
        self.lista_Hotels=[]
        f = open("src/API/Airhopping/Booking.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            if id==ID:
                linea = f.readline()
                nombre=linea
                linea = f.readline()
                precio=linea
                f.close()
                HotelDict = {
                    "ID": id,
                    "Nombre": nombre,
                    "precio": precio,
                }
                return HotelDict
            else:
                linea = f.readline()
                linea = f.readline()

            linea = f.readline()


        f.close()
        return "No encontrado"

    def confirm_reserve(self, user, hotels):

        return True
