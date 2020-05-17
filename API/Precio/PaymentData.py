#La classe 'PaymentData' 'PaymentData' conté les dades necessàries per poder efectuar el pagament:
#    - Tipus de targeta : VISA o Mastercard
#    - Nom del titular (el que apareix a la targeta)
#    - Número de la targeta
#    - Codi de seguretat
#    - Import

class PaymentData:

    def __init__(self, metodo, nom_titular, num_cuenta, codigo_s, importe):
        self.metodo = metodo
        self.nom_titular = nom_titular
        self.num_cuenta = num_cuenta
        self.codigo_s = codigo_s
        self.importe = importe