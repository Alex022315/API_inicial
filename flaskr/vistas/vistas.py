from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema, Album, AlbumSchema, Usuario, UsuarioSchema
from flask import request

cancion_schema = CancionSchema()
album_schema = AlbumSchema()
usuario_schema = UsuarioSchema()

class VistaCanciones(Resource):
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(
            titulo=request.json['titulo'],
            minutos=request.json['minutos'],
            segundos=request.json['segundos'],
            interprete=request.json['interprete']
        )
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

class VistaCancion(Resource):
    def get(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        return cancion_schema.dump(cancion)

    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operación exitosa', 204

class VistaAlbumes(Resource):
    def get(self):
        return [album_schema.dump(album) for album in Album.query.all()]

class VistaAlbum(Resource):
    def get(self, id_album):
        album = Album.query.get_or_404(id_album)
        return album_schema.dump(album)

    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get('titulo', album.titulo)
        album.year = request.json.get('year', album.year)
        album.descripcion = request.json.get('descripcion', album.descripcion)

        db.session.commit()
        return album_schema.dump(album)

    def delete(self, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return 'Operación exitosa', 204

class VistaUsuarios(Resource):
    def get(self):
        return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]

