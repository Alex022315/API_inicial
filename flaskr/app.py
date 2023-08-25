from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio
import enum
app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = Usuario(nombre= 'Juan', contrasena='12345')
    a = Album(titulo='prueba', ano=1999, descripcion='Como el vino', medio=Medio.cd)
    c = Cancion(titulo='Mi cancion', minutos=1, segundos=15, interprete='Xander')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].canciones)
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())

