#import User as User
#import User_ini as User_ini
#import Cars as Cars






class Rentalcars:

    def __init__(self):
        pass

    def buscar_coche(self,ID):
        f = open("src/API/Coche/Rentalcars.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            id=id.replace('\n','')
            id=id.replace(' ','')
            if id==ID:
                linea = f.readline()
                linea=linea.replace('\n','')
                linea=linea.replace(' ','')
                nombre=linea
                linea = f.readline()
                linea=linea.replace('\n','')
                linea=linea.replace(' ','')
                precio=linea
                f.close()
                CocheDict = {
                    "Matricula": id,
                    "Nombre": nombre,
                    "precio": precio,
                }
                return CocheDict
            else:
                linea = f.readline()
                linea = f.readline()

            linea = f.readline()


        f.close()
        return  "No encontrado"

    def confirm_reserve(self, user, cars):
        return True
