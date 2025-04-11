from flask import Flask
from config import Config
from modelos.contacts import Contacto
from modelos.users import Usuario
from schemas.contact_schema import ContactoSchema
from schemas.user_schema    import UserSchema
from routes.contact_rutes import contacto_bp
from routes.user_rutes import usuario_bp
from extensions import db, ma, init_jwt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
from flasgger import Swagger




def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY']     = os.getenv('JWT-SECRET_KEY')  # clave secreta de prueba
    app.config["API_TITLE"]          = "Contacts API"
    app.config["API_VERISION"]       = "v1"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    load_dotenv()

    # Iniciando las extensiones
    db.init_app(app)
    ma.init_app(app)
    init_jwt(app)
    
    # Migraciones
    migrate = Migrate(app, db)    


    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API REST Contactos",
            "description": "Documentación Swagger de mi API de Contactos en Flask",
            "version": "1.0"
        },
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Token JWT usando el esquema Bearer. Ejemplo: 'Bearer {token}'"
            }
        }
    }

    Swagger(app, template=swagger_template)
            
    # Blueprints    
    app.register_blueprint(contacto_bp, url_prefix='/api')
    app.register_blueprint(usuario_bp , url_prefix='/api')

    return app



if __name__ == '__main__':
    create_app.run(debug=True)




# @app.cli.command('db_create')
# def db_create():
#     db.create_all()
#     print('Base de datos creada exitosamente !')


# @app.cli.command('db_drop')
# def db_drop():
#     db.drop_all()
#     print('Base de datos eliminada')


# # Definicion de los datos a partir del modelo Contacto
# @app.cli.command('db.seed')
# def db_seed():
#     usuario = Usuario(id=None,
#                       username='Admin',
#                       password='admin12345')       

#     db.session.add(usuario)

#     db.session.commit()
#     print(f'Base de datos {usuario} creada y poblada')



