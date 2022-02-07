from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_required, login_user, logout_user

from app.models.ModeloUsuario import ModeloUsuario



from .models.ModeloLibro import ModeloLibro

from .models.entities.Usuario import Usuario
from .consts import *
from .models.ModeloUsuario import ModeloUsuario

app = Flask(__name__)

crsf = CSRFProtect()
db = MySQL(app)
login_namager_app = LoginManager(app)

@login_namager_app.user_loader
def loader_user(id):
    return ModeloUsuario.obtener_por_id(db, id)

@app.route('/')
#decorador para requerir autenticacion obligatoria
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    # CSRF (Cross-Site Request Forgery): Solicitud de falsificacion entre sitios
    if request.method == 'POST':
        usuario =  Usuario(None, request.form['usuario'], request.form['password'],None)
        usuario_logueado = ModeloUsuario.login(db,usuario)
        if usuario_logueado != None:
            login_user(usuario_logueado)
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALES_INVALIDAS, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))

@app.route('/libros')
@login_required
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

def pagina_no_autorizada(error):
    return redirect(url_for('login'))

def inicializar_app(config):
    app.config.from_object(config)
    crsf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, pagina_no_encontrada)
    return app