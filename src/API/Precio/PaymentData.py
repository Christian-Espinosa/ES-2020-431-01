#La classe 'PaymentData' 'PaymentData' conté les dades necessàries per poder efectuar el pagament:
#    - Tipus de targeta : VISA o Mastercard
#    - Nom del titular (el que apareix a la targeta)
#    - Número de la targeta
#    - Codi de seguretat
#    - Import

class PaymentData:

    def __init__(self):
        self.metode=""
        self.titular=""
        self.numero=""
        self.codi_seg=""
        self.importe=""

    def leer_datos(self):
        self.lista_Vuelos=[]
        f = open("src/API/Precio/PaymentData.txt")
        linea = f.readline()
        while linea != "":
            titular=linea
            if titular==self.titular:
                linea = f.readline()
                numero=linea
                linea = f.readline()
                codi_seg=linea
                linea = f.readline()
                metodo=linea
                linea = f.readline()
                importe=linea
                f.close()
                PaymentDict = {
                    "Titular": titular,
                    "Numero": numero,
                    "Codigo seguridad": codi_seg,
                    "Metodo":metodo,
                    "Importe":importe,
                }
                return PaymentDict
            else:
                linea = f.readline()
                linea = f.readline()
                linea = f.readline()
                linea = f.readline()

            linea = f.readline()


        f.close()
        return  "No encontrado"
