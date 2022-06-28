import json
class Homelib:                                      
    def __init__(self):
        try:
            with open("homelib.json", "r") as f:  
                self.homelib = json.load(f)       
        except FileNotFoundError:
            self.homelib = []                     

########## dla każdego odczytanego elementu dodac id - pętla for - popcząwszy od 0  -- od wiersza po 8 lub 11 


    def all(self): 
        return self.homelib                       

    def get(self, id):  
        return self.homelib[id]
        ## PRÓBA MENT 1: homelibrary = [homelibrary for homelibrary in self.all() if homelibrary['id'] == id] # MODYFIKACJA #1  metody get bo: chcemy pobierać obiekt na podstawie zapisanego id. Może się zdarzyć, że to id nie będzie w naszej liście, stąd dodatkowy if.
        #if homelibrary:
        #    return homelibrary[0]
        #return []                   

    ## dlaczego w metodzie poniżej usuwamy data.pop- tak jak w przykładzie moduł 7.4 - JEST OK - UZGODNIONE Z MENTOREM 
    def create(self, data): 
        data.pop('csrf_token')   ## PRÓBA MENT 1 - MA   TO USUNĄĆ :
        self.homelib.append(data)
        # ## PRÓBA MENT 1:self.save_all()                  

    def save_all(self): 
        with open("homelib.json", "w") as f:       
            json.dump(self.homelib, f)              

    # poniższe działano w wersji pierwotnej - przed REST-API
    #def update(self, id, data): 
    #    data.pop('csrf_token')
    #    self.homelib[id] = data                        
    #    self.save_all()

    def update(self, id, data):
        homelibrary = self.get(id)
        if homelibrary:
            index = self.homelib.index(homelibrary)
            self.homelib[index] = data
            self.save_all()
            return True
        return False


    def delete(self, id): 
        homelibrary = self.get(id)
        if homelibrary:
            self.homelib.remove(homelibrary)
            self.save_all()
            return True      # Jeśli znajdziemy odpowiednie todo, to możemy je usunąć i zwracamy wtedy True. W przeciwnym wypadku zwrócimy False. 
        return False     

homelib = Homelib()                                 




#TodoForm > HomelibraryForm
# todos > homelib
# todo > homelibrary  # todo_id > homelibrary_ud
# Todos > Homelib