from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response
from forms import HomelibraryForm                   
from models import homelib                          

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"



@app.route("/homelib/", methods=["GET", "POST"])   
def homelib_list():                                  
    form = HomelibraryForm()                        
    error = ""
    if request.method == "POST":  
        if form.validate_on_submit():
            homelib.create(form.data)                 
            homelib.save_all()                        
        return redirect(url_for("homelib_list"))       
    return render_template("homelib.html", form=form, homelib=homelib.all(), error=error)    
    

@app.route("/homelib/<int:homelibrary_id>/", methods=["GET", "POST"])  
def homelibrary_details(homelibrary_id):                            
    homelibrary = homelib.get(homelibrary_id - 1)
    form = HomelibraryForm(data=homelibrary)         
    if request.method == "POST":   
        if form.validate_on_submit():
            homelib.update(homelibrary_id - 1, form.data)       
        return redirect(url_for("homelib_list"))        
    return render_template("homelibrary_id.html", form=form, homelibrary_id=homelibrary_id)  

#  mowe końcówki uwględniające REST  


@app.route("/api/v1/homelib/", methods=["GET"]) 
def homelib_list_api_v1(): 
    return jsonify(homelib.all())

## #1: końcówka  - funkcja do pobierania  danych wg ID - GET
@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=["GET"]) 
def get_homelibrary(homelibrary_id):
    homelibrary = homelib.get(homelibrary_id)
    if not homelibrary:    
        abort(404)   
    return jsonify({"homelibrary": homelibrary})


@app.errorhandler(404)  
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

## #2 - końcówka  - funkcja do  dodawania nowego elementu homelibrary  - POST

## UZGODNIONE Z MENTOREM -  NIE TRZEBA : czy w związku z nowym elementem 'id' - nie należy także dokonac modyfikacji w "forms.py" - test API , gdy wybieram metodę inną niż GET - bez podawania id nie powiodło się

@app.route("/api/v1/homelib/", methods=["POST"]) 
def create_homelibrary():
    if not request.json or not 'title' in request.json:
        abort(400)
    homelibrary = {
        'id': homelib.all()[-1]['id'] + 1, # bierze ostatni nr ID (-1)  i dodaje do niego 1  . zwiększa nr ID - 
        'title': request.json['title'], 
        'description': request.json.get('description', ""),  
        'done': False
    }
    homelib.create(homelibrary)
    return jsonify({'homelibrary': homelibrary}), 201  # Zauważmy też, że zwracana jest para wartości w przypadku sukcesu: return jsonify({'task': task}), 201. Kod 201 ma opis “Created”. To dokładnie ta sytuacja, w której chcemy go użyć. 

# dodac default -none id


@app.errorhandler(400) # MODYFIKACJA 2.1 - dodanie kolejnego błędu gdy gdyby ktoś zapomniał o danych obligatoryjnych   
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


## #3 - końcówka  - funkcja do usuwania tasków  - DELETE
@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=['DELETE'])  
def delete_homelibrary(homelibrary_id):
    result = homelib.delete(homelibrary_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


## # 4 - końcówka  - funkcja do nadpisywania  tasków - PUT
@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=["PUT"])
def update_homelibrary(homelibrary_id): 
    homelibrary = homelib.get(homelibrary_id)  # Po pierwsze sprawdzamy, czy todo o takim id istnieje. Jeśli nie, to wiadomo: 404. 
    if not homelibrary:
        abort(404)
    if not request.json: # Sprawdzamy, czy przesyłane są dane – jeśli nie to 400.
        abort(400)
    data = request.json  # Ten sam błąd powinien polecieć, kiedy ktoś wpisze jakieś dziwne dane w nasze pole. Np. done może być tylko typu bool, a tytuł i opis powinny być tekstem. Użyliśmy tu any, by nie tworzyć wielu ifów.
    # Sprawdzenia instancji chcemy dokonać tylko wtedy, gdy dane pole jest w przychodzących danych, czyli w request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)   
    #  Dalej przygotowujemy todo w nowe wersji. Jeśli danych nie ma request.json, to bierzemy je ze starego obiektu
    homelibrary = {
        'title': data.get('title', homelibrary['title']),
        'description': data.get('description', homelibrary['description']),
        'done': data.get('done', homelibrary['done'])
    }
    # Robimy update i już. Tym razem w update nie musimy już sprawdzać, czy dany obiekt istnieje. Przed chwilą to zrobiliśmy, ale z drugiej strony, można by to tam dodać w przyszłości, jeśli metoda będzie wykorzystywana jakoś inaczej.
    homelib.update(homelibrary_id, homelibrary)
    return jsonify({'homelibrary': homelibrary})


if __name__ == "__main__":
    app.run(debug=True)


#TodoForm > HomelibraryForm
# todos > homelib
# todo > homelibrary
# Todos > Homelib