from flask import Flask
#from .modelos import db, Cancion
def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://root@localhost/flaskmysql'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
