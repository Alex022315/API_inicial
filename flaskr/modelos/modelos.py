from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class EnumADiccionario(fields.Field):
    def _serialize(
        self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}


class EnumADiccionario(fields.Field):
    def _serialize(
        self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}

class AlbumSchema(SQLAlchemyAutoSchema):
    medio =EnumADiccionario(atrtibute=('medio'))
    class Meta:
        model = Album
        include_relationships= True
        load_instance = True

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary = 'album_cancion', back_populates='canciones')

class Medio(enum.Enum):
    DISCO= 1
    CASETE = 2
    CD = 3



class Usuario(db.Model):
    tablename = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String)
    contrasena = db.Column(db.String(350))
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary = 'album_cancion', back_populates='albumes')
    __table__args__ = (db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_album'),)

albumes_canciones = db.Table('album_cancion', \
                              db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_Key=True), \
                              db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True))
