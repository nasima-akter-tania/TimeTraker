
class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///timetraker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'
    JWT_SECRET_KEY =  'jwt-secret-string'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass