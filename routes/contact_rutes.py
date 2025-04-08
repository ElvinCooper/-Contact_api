from flask import Blueprint, request, jsonify
from app import db
from modelos.contacts import Contacto
from schemas.contact_schema import ContactoSchema
from marshmallow.exceptions import ValidationError

contacto_bp = Blueprint('contactos', __name__)
contacto_schema = ContactoSchema()
contacts_schema = ContactoSchema(many=True)



# Enpoint inicial  
@contacto_bp.route('/')
def index():
    return jsonify({"message": "API de Contactos activa"}), 200


# Enpoint para consultar todos los datos de la tabla de contactos
@contacto_bp.route('/contactos', methods=['GET'])
def listar_contactos():
    list_contacts = Contacto.query.all()    
    
    return jsonify(contacts_schema.dump(list_contacts))



# Endpoint para consultar un contacto con su id
@contacto_bp.route('/contactos/<int:id>' , methods=['GET'])
def get_contactos(id):
    contacto = Contacto.query.get_or_404(id)
           
    return jsonify(contacto_schema.dump(contacto)), 200    



# Enpoint para insertar un contacto
@contacto_bp.route('/contactos', methods=['POST'])
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
@contacto_bp.route('/contactos/<int:id>', methods=['PUT'])   
def actualizar_contacto(id):
    contacto = Contacto.query.get_or_404(id)

    try:
        data = ContactoSchema().load(request.get_json(), partial=True)
        if 'nombre' in data:
            contacto.nombre = data['nombre']
        if 'email' in data:
            contacto.email = data['email']   

        db.session.commit()
        
        return jsonify(contacto_schema.dump(contacto))               
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400
    except Exception as err:
        return jsonify({"Error": str(err)}), 400    
    



# ENDPOINT PARA ELIMINAR UN RECURSO DE LA BD
@contacto_bp.route('/contactos/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contacto = Contacto.query.get_or_404(id)

    db.session.delete(contacto)
    db.session.commit()
    return jsonify({"mensaje": f"Registro '{contacto.nombre}' eliminado exitosamente"}), 200    