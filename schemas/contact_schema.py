# definicion del schema marshmallow    
from marshmallow import  Schema, fields, validate
from models import Contacto


class ContactoSchema(Schema):
    id     = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1))
    email  = fields.Email(required=True)
