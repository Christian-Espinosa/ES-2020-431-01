 from Viatger import Viatger

class Viatgers:
    viatgers=[]
    num_viatgers=0
    def __init__(self):
        self.viatgers=[]
        self.num_viatgers=0

    def get_num_viatgers(self):
      return self.num_viatgers

    def get_viatgers(self):
        tempList=[]
        for v in self.viatgers:
          tempList.append(v.get_name())
        return tempList

    def add_viatger(self, name:str):
        self.viatgers.append(Viatger(name))
        self.num_viatgers=self.num_viatgers+1

    def remove_viatger(self,name:str):
        for i in self.viatgers:
            if i.get_name()==name:
                self.viatgers.remove(i)
                self.num_viatgers=self.num_viatgers-1

   