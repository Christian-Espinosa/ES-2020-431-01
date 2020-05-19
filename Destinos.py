import Destino as Destino


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

    def get_destino(self,id):
        temp_Ret=None
        for i in self.destinos:
            if i.get_id()==id:
                temp_Ret=i
        return temp_Ret
    
    def add_destino(self,id,vuelo,hotel):
        self.destinos.append(Destino.Destino(id,vuelo,hotel))
        self.num_destinos=self.num_destinos+1

    def remove_destino(self,id):
        for i in self.destinos:
            if i.get_id()==id:
                self.destinos.remove(i)
                self.num_destinos=self.num_destinos-1

   