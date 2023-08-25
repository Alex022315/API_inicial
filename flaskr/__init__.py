from flask import Flask
#from .modelos import db, Cancion
def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLACLCHEMY_DATABASE_URI'] ='sqlite:///tutorial_cancioes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
