from flask_script import Manager, Server
from app import inicializar_app
from flask_script._compat import text_type
from config import config


configuracion=config['development']
app = inicializar_app(configuracion)

#Instancia de Manager pasandole las app
manager = Manager(app)
manager.add_command('runserver',Server(host='0.0.0.0',port=5000))

if __name__ == '__main__':
    manager.run()

