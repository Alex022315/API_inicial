from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema

cancion_schema = CancionSchema()

class VistaCanciones(Resource):
    def get(self):
        return [cancion_schema.dump(Cancion)for Cancion in Cancion.query.all()]