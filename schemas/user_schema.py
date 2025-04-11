from marshmallow import  Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from modelos.users import Usuario
from extensions import ma


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
                        
    id       = fields.String(dump_only=True)  
    username = auto_field(required=True, validate=validate.Length(min=1, max=60))
    password = auto_field(required=True, validate=validate.Length(min=8, max=25))
    