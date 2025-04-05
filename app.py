from flask import Flask, request, jsonify
from config import Config
from models import db, Contacto
import sqlite3, requests
from schemas import ContactoSchema
from marshmallow.exceptions import ValidationError


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


# Enpoint inicial  
@app.route('/')
def index():
    return jsonify({"message": "API de Contactos activa"}), 200



# Enpoint para consultar todos los datos de la tabla de contactos
@app.route('/contactos' , methods=['GET'])
def contactos():
    list_contacts = Contacto.query.all()    
    
    return jsonify(contacts_schema.dump(list_contacts))



# Endpoint para consultar un contacto con su id
@app.route('/contactos/<int:id>' , methods=['GET'])
def get_contacto(id):
    contacto = Contacto.query.get_or_404(id)
           
    return jsonify(contacto_schema.dump(contacto)), 200



 # Enpoint para insertar un contacto
@app.route('/contactos', methods=['POST'])
def crear_contacto():
    try:
        json_data = request.get_json()
        data = contacto_schema.load(json_data)

        if Contacto.query.filter_by(email=data['email']).first():
            return jsonify({"mensaje": "Ya existe un contacto con este email"}), 400

        nuevo_contacto = Contacto(**data)
        db.session.add(nuevo_contacto)
        db.session.commit()

        return jsonify(contacto_schema.dump(nuevo_contacto)), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    


# Endpoint para actualizar un recurso en la bd
@app.route('/contactos/<int:id>', methods=['PUT'])   
def actualizar_contacto(id):
    contacto = Contacto.query.get_or_404(id)

    try:
        data = ContactoSchema().load(request.get_json(), partial=True)
        if 'nombre' in data:
            contacto.nombre = data['nombre']
        if 'email' in data:
            contacto.email = data['email']   

        db.session.commit()
        
        return jsonify(contacto_schema.dump(contacto))                 #jsonify(contacto_schema.dump(contacto))
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400
    except Exception as err:
        return jsonify({"Error": str(err)}), 400
                


# ENDPOINT PARA ELIMINAR UN RECURSO DE LA BD
@app.route('/contactos/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contacto = Contacto.query.get_or_404(id)

    db.session.delete(contacto)
    db.session.commit()
    return jsonify({"mensaje": f"Registro '{contacto.nombre}' eliminado exitosamente"}), 200


if __name__ == '__main__':
    app.run(debug=True)