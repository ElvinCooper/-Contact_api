from flask import Flask, request, jsonify
from config import Config
from modelos.contacts import Contacto, db
import requests
#from esquemas.contact_schema import ContactoSchema
from schemas.contact_schema import ContactoSchema
import config
from routes.contact_rutes import contacto_bp

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


contacto_schema = ContactoSchema()
contacts_schema = ContactoSchema(many=True)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Base de datos creada exitosamente !')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Base de datos eliminada')


# Definicion de los datos a partir del modelo Contacto
@app.cli.command('db.seed')
def db_seed():
    contacto1 = Contacto(id=None,
                         nombre='Andrew',
                         email='andrew@gmail.com')
    
    contacto2 = Contacto(id=None,
                         nombre='Elvin',
                         email='elvin@gmail.com')
    
    contacto3 = Contacto(id=None,
                         nombre='Katherin',
                         email='katherin@gmail.com')

    db.session.add(contacto1)
    db.session.add(contacto2)
    db.session.add(contacto3)

    db.session.commit()
    print('Base de datos poblada')


# REGISTRAR LOS BLUEPRNTS
app.register_blueprint(contacto_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)