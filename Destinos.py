from Destino import Destino

class Destinos:
    destinos=[]
    num_destinos=0
    def __init__(self):
        self.destinos=[]
        self.num_destinos=0

    def get_num_destinos(self):
      return self.num_destinos

    def get_lista_destinos(self):
        tempList=[]
        for d in self.destinos:
          tempList.append(d)
        return tempList

    def add_destino(self,id,vuelo,hotel,precio):
        self.destinos.append(Destino(id,vuelo,hotel,precio))
        self.num_destinos=self.num_destinos+1

    def remove_destino(self,id):
        for i in self.destinos:
            if i.get_id()==id:
                self.destinos.remove(i)
                self.num_destinos=self.num_destinos-1

   