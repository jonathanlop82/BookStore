class config:
    pass

#Para activar el modo debug
class DevelopmentConfig(config):
    DEBUG=True

config={
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}