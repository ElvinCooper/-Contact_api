from flask import Flask, request, jsonify
import re, os
import sqlite3, requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mis_contactos.db')


db  = SQLAlchemy(app)
ma = Marshmallow(app)



class Contacto(db.Model):
    __tablename__ = 'mis_contactos'
    id     = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email  = Column(String, nullable=False)

# definicion del schema marshmallow    
class ContactoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contacto
        load_instance = True


contacto_schema = ContactoSchema()  # esquema para la serializacion de los datos


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




# Enpoint para consultar todos los datos de la tabla de contactos
@app.route('/contactos' , methods=['GET'])
def contactos():
    list_contacts = Contacto.query.all()
    contacto_schema = ContactoSchema(many=True)
    
    return jsonify(contacto_schema.dump(list_contacts))



# Endpoint para consultar un contacto con su id
@app.route('/micontacto/<int:id>' , methods=['GET'])
def get_contacto(id):
    contacto = Contacto.query.get_or_404(id)
        
    contacto_schema = ContactoSchema()
    return jsonify(contacto_schema.dump(contacto))



#Enpoint para insertar un contacto
@app.route('/insertar/<string:nombre>/<string:email>', methods=['POST'])
def put_contact(nombre: str, email: str): 
    data = request.get_json(silent=True)

    if not nombre or not email:
        return jsonify({"Mensaje": "Faltan parametros (nombre y/o email)"}), 400
    
    # Validar formato de email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"Error": "Formato de email inválido"}), 400

    
    #email = data.get("email")
    if Contacto.query.filter_by(email=email).first():
        return jsonify({"Mensaje": "Ya existe un contacto con este email"}), 400

    nuevo_contacto = Contacto(nombre = nombre,
                              email  = email)
    
    db.session.add(nuevo_contacto)
    db.session.commit()

    #contacto_schema = ContactoSchema()
    return jsonify(contacto_schema.dump(nuevo_contacto)), 201
    


# Endpoint para actualizar un contacto con su id
@app.route('/update/<int:id>' , methods=['PUT'])
def update_contacto(id, nombre, email):
    contacto = Contacto.query.get_or_404(id)

    data = request.get.json()
    if 'name' in data:
        contacto.name = data['name']
    
    if 'email' in data:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"Error": "Formato de email inválido"}), 400
        
        contacto.email = data['email']

    db.session.commit()
    return contacto_schema.jsonify(contacto)

    #return jsonify(contacto_schema.dump(contacto))


if __name__ == '__main__':
    app.run(debug=True)