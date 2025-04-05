from marshmallow import  Schema, fields, validate
from marshmallow.exceptions import ValidationError
from models import Contacto


# definicion del schema marshmallow    
class ContactoSchema(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)