from flask import Flask, request, render_template, redirect, url_for

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


if __name__ == "__main__":
    app.run(debug=True)


#TodoForm > HomelibraryForm
# todos > homelib
# todo > homelibrary 