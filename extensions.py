from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


db  = SQLAlchemy()
ma  = Marshmallow()
jwt = JWTManager()


def init_jwt(app):
    jwt.init_app(app)

    # manejador personalizado
    @jwt.unauthorized_loader
    def custom_unauthorized_response(err_msg):
        return {
            "error": "No autorizado",
            "descripcion": "Falta el token o el encabezado Authorizacion no esta presente."
        }, 401
