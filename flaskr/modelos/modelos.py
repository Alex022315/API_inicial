from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class Medio(db.Model):
    disco = db.Column(db.String(128))
    casete = db.Column(db.String(128))
    cd = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}".format(self.disco, self.casete, self.cd)

class Usuario(db.Model):
    tablename = db.Column(db.String(128))
    id = db.Column(db.Integer)
    nombre_usuario = db.Column(db.String)
    contrasena = db.Column(db.String(350))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.tablename, self.id, self.nombre_usuario, self.contrasena)

class Album(db.Model):
    tablename__ = db.Column(db.String(128))
    id = db.Column(db.Integer)
    titulo = db.Column(db.String(128))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Medio)

    def __repr__(self):
        return "{}-{}-{}-{}-{}-{}".format(self.tablename__, self.id, self.titulo, self.ano, self.descripcion, self.medio)
