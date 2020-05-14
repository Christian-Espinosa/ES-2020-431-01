import User_ini as User_ini

class User:
    def __init__(self):
        self.lista_User=[]
        f = open("API/Usuarios.txt")
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

            self.lista_User.append(User_ini.User_ini(nombre,DNI,calle,tel,email))
            linea = f.readline()

        


        f.close()


    def getDatosUser(self, DNI):
        for i in self.lista_User:
            if i.get_DNI()==DNI:
               return i.getDatosUser()
               
        return "No existe el usuario"
            
        