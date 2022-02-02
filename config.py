class config:
    SECRET_KEY = 'nQ=;8nGEbr!!gZNeD>!d#7W'

#Para activar el modo debug
class DevelopmentConfig(config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'tienda'

config={
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}