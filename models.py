import json
from flask import make_response, jsonify


# PRÓBA 1:  co jest w homelib?

#with open("./homelib.json", "r") as f:  
#   homelib = json.loads(f)
#   print(type(homelib)) 
#   print(homelib)

# WYNIK:
## with open("homelib.json", "r") as f:
## FileNotFoundError: [Errno 2] No such file or directory: 'homelib.json'

# PRÓBA 2:  co jest w homelib? 
# with open("homelib.json", "r") as f:  
#    homelib = json.load(f)
#    for index in range(len(homelib)):
#        for key in homelib[index]:
#            print(homelib[index][key]) 

# WYNIK:
## with open("homelib.json", "r") as f:
## FileNotFoundError: [Errno 2] No such file or directory: 'homelib.json'

# PRÓBA 3: tylko utworzenie nowego elementu: 
#with open("homelib.json", "r") as f:  
#    homelib = json.load(f)
#    for index in range(len(homelib)):
#        homelib["id"]=1
#        print(homelib)

# WYNIK:
## with open("homelib.json", "r") as f:
## FileNotFoundError: [Errno 2] No such file or directory: 'homelib.json'

# PRÓBA 4:  ..... 
#with open("./homelib.json", "r") as f:  
# ....

# WYNIK:
## with open("homelib.json", "r") as f:
## FileNotFoundError: [Errno 2] No such file or directory: './homelib.json'

#LOOP
# for index in range(len(self.homelib)):
#    self.homelib[index]['id'] = index

###     for key in self.homelib[index]:
###     print(self.homelib[index][key])  



class Homelib:                                      
    def __init__(self):
        try:
            with open("homelib.json", "r") as f:  
                self.homelib = json.load(f)
                for index in range(len(self.homelib)):
                    self.homelib[index]['id'] = index       
        except FileNotFoundError:
            self.homelib = []                     

########## dla każdego odczytanego elementu dodac id - pętla for - popcząwszy od 0  -- od wiersza po 8 lub 11 


    def all(self): 
        return self.homelib                       

    def get(self, id):  
        if id not in self.homelib:
            response=jsonify({'error': 'Not found', 'status_code': 404})
            response.status_code=404
            return response ####### jeżeli jest OK to ma pokazać FALSE - jak nie to ma pokazać TRUE 
        return self.homelib[id] , ####### jeżeli jest OK to ma pokazać TRUE - jak nie to ma pokazać fałsz 
        ## PRÓBA MENT 1: homelibrary = [homelibrary for homelibrary in self.all() if homelibrary['id'] == id] # MODYFIKACJA #1  metody get bo: chcemy pobierać obiekt na podstawie zapisanego id. Może się zdarzyć, że to id nie będzie w naszej liście, stąd dodatkowy if.
        #if homelibrary:
        #    return homelibrary[0]
        #return []                   

    ## dlaczego w metodzie poniżej usuwamy data.pop- tak jak w przykładzie moduł 7.4 - JEST OK - UZGODNIONE Z MENTOREM 
    def create(self, data): 
        # data.pop('csrf_token')   ## PRÓBA MENT 1 - MA   TO USUNĄĆ :
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