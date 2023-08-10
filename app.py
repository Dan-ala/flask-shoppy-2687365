from flask import Flask #First thing to do
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

#Creation and setting-up of the app
app=Flask(__name__) #__name__ is a variable and indicates the module's name in this case, app.
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/flask_shoppy_2687365" # This command indicates what is the db that I will be working on
#The objects SQLAlchemy are created
db = SQLAlchemy(app)
migrate=Migrate(app,db) #This is an object it has two parameters


#modules
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(120))

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision=10, scale=2))
    imagen = db.Column(db.String(100))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

class Detalle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'))
    cantidad = db.Column(db.Integer)