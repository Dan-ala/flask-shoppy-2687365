from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap


class NewProductForm(FlaskForm):
    nombre = StringField('Ingrese producto: ')
    precio = StringField('Ingrese precio: ')
    submit = SubmitField('Registrar')