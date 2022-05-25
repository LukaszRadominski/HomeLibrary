import json


class Homelib:                                      
    def __init__(self):
        try:
            with open("homelib.json", "r") as f:  
                self.homelib = json.load(f)       
        except FileNotFoundError:
            self.homelib = []                     

    def all(self): 
        return self.homelib                       

    def get(self, id):  
        return self.homelib[id]                   

    def create(self, data): 
        data.pop('csrf_token') 
        self.homelib.append(data)                  

    def save_all(self): 
        with open("homelib.json", "w") as f:       
            json.dump(self.homelib, f)              

    def update(self, id, data): 
        data.pop('csrf_token')
        self.homelib[id] = data                        
        self.save_all()


homelib = Homelib()                                 


# todos > homelib
# Todos > Homelib
