from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#UserMixin clase de flask_login necesaria para loguearse en flask
class Usuario(UserMixin):

    def __init__(self, id, usuario, password, tipousuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    @classmethod
    def verificar_password(self, encriptado, password):
        coincide = check_password_hash(encriptado, password)
        return coincide