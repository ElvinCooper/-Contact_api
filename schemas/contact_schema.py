from marshmallow import  Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Contacto
from extensions import ma


class ContactoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Contacto
        load_instance = True
                              
    id             = fields.UUID(dump_only=True)  
    nombre         = auto_field(required=True, validate=validate.Length(min=1))
    email          = auto_field(required=True, validate=validate.Email(error="Email Invalido"))
    telefono       = fields.String(validate=validate.Length(min=7, max=20))
    fecha_creacion = fields.Date(dump_only=True)

