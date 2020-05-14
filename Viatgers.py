import Viatger.py

class Viatgers:
    def __init__(self, name:str):
        self.viatgers=[]
        self.num_viatgers=0

    def get_viatgers(self)->str:
        return self.viatgers

    def add_viatger(self, name:str):
        temp = Viatger.__init__(name)
        self.viatgers.append(temp)
        self.num_viatgers=self.num_viatgers+1

    def remove_viatger(self, name:str):
        for i in self.viatgers:
            if i.get_name()==name:
                self.viatgers.remove(i)
                self.num_viatgers=self.num_viatgers-1

   