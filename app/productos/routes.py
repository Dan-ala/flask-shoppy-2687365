from . import productos
from flask import render_template
from .forms import NewProductForm
import app
import os #Me permite trabajar con los archivos del OS

#Crear las rutas del blueprint
@productos.route('/crear', methods=["GET","POST"])
def crear():
    p=app.models.Producto()
    form=NewProductForm()
    if form.validate_on_submit():
        # EL formulario va a llenar
        # El nuevo objeto producto
        # automaticamente 
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()

        #Ubicar el archivo IMAGEN en la carpeta, app/productos/imagenes
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd() + '/app/productos/imagenes/' + p.imagen)) #Establecer un puntero a una carpeta en particular

        return 'Producto Registrado'
    return render_template("new.html", form=form)

@productos.route('/listar')
def listar():
    #PRIMERO: Traemos los productos de la db
    productos = app.Producto.query.all()
    #SEGUNDO: Mostrar la vista de listar, pero enviándole los productos seleccionados por la consulta
    return render_template('listar.html',
                           productos=productos) #el primer 'producto' es un alias