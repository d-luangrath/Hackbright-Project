import os

class BaseConfig(object):
    DEBUG = True
    DB_NAME = "recipes"
    DB_USER = "darla"
    DB_PASS = "mys3cretpassw0rd!"
    DB_PORT = 5437
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@postgres:{DB_PORT}/{DB_NAME}'


pass