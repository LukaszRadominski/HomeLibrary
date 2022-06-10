from flask_wtf import FlaskForm             
from wtforms import StringField, BooleanField, TextAreaField, IntegerField  
from wtforms.validators import DataRequired 



class HomelibraryForm(FlaskForm):  
    done = BooleanField('Czy przeczytałeś?', validators=[DataRequired()])
    title    = StringField('Podaj tytuł książki', validators=[DataRequired()])
    description = TextAreaField('Streść książkę', validators=[DataRequired()])
    

  


#TodoForm > HomelibraryForm
# todos > homelib
# todo > homelibrary
# Todos > Homelib

 
    

