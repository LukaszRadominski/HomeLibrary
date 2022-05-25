from flask_wtf import FlaskForm             
from wtforms import StringField, BooleanField, TextAreaField  
from wtforms.validators import DataRequired 



class HomelibraryForm(FlaskForm):  
    checkbox = BooleanField('Czy przeczytałeś?', validators=[DataRequired()])
    title    = StringField('Podaj tytuł książki', validators=[DataRequired()])
    description = TextAreaField('Streść książkę', validators=[DataRequired()])


 
    

