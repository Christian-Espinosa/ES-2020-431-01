class User_ini:
    def __init__(self, NombreCompleto, DNI, DirPostal, NumTel, Email):
        self.NombreCompleto = NombreCompleto
        self.DNI = DNI
        self.DirPostal = DirPostal
        self.NumTel= NumTel
        self.Email= Email


    def getDatosUser(self):
        UserDict = {
            "Nombre": self.NombreCompleto,
            "DNI": self.DNI,
            "DirPostal": self.DirPostal,
            "NumTel":self.NumTel,
            "Email":self.Email
            }

            
        return UserDict
        
    def get_DNI(self):
        return self.DNI