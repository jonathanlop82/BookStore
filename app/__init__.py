from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.ModeloLibro import ModeloLibro

app = Flask(__name__)

crsf = CSRFProtect()
db = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # CSRF (Cross-Site Request Forgery): Solicitud de falsificacion entre sitios
    if request.method == 'POST':
        if request.form['usuario'] == 'admin1' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        print(ex)

#Funcion para enviar un mensaje de retorno de error 404
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

def inicializar_app(config):
    app.config.from_object(config)
    crsf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app