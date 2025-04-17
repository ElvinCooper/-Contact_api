from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from modelos.users import Usuario
from routes.contact_rutes import contacto_bp
from routes.user_rutes import usuario_bp
from extensions import db, init_extensions, migrate
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flasgger import Swagger




def create_app(testing=False): 

    app = Flask(__name__)
    load_dotenv()
    

    # detectar el entorno desde .FLASKENV
    env = os.getenv("FLASK_ENV", "development")

    if testing:
        app.config.from_object(TestingConfig)
    elif env == "production":    
        app.config.from_object(ProductionConfig)
        
    else:
        app.config.from_object(DevelopmentConfig) 




    # Inicializar CORS para permitir solicitudes desde el frontend
    frontend_url = app.config.get('FRONTEND_URL', 'http://localhost:3000')  # Valor por defecto
    if not frontend_url:
        raise ValueError("FRONTEND_URL debe estar definido en la configuración.")
    
    # Inicializar CORS para permitir solicitudes desde el frontend
    CORS(app, resources={r"/api/*": {"origins": frontend_url,
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }})

    # Iniciando las extensiones
    init_extensions(app)
    migrate = Migrate(app, db) 
   
    # Swagger
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


app = create_app()


with app.app_context():
    db.create_all()
    print("Intentando crear la base de datos al inicio de la aplicación.")


# Comando para crear la base de datos
@app.cli.command('db_create')
def db_create():
    with app.app_context():
        db.create_all()
        print('Base de datos creada exitosamente !')


# comando para eliminar la base de datos
@app.cli.command('db_drop')
def db_drop():
    with app.app_context():
        db.drop_all()
        print('Base de datos eliminada')


# comando para insertar datos iniciales
@app.cli.command('db.seed')
def db_seed():
    with app.app_context():
        usuario = Usuario(id=None,
                        username='Admin',
                        password='admin123',
                        email="ing.elvin01cooper@gmail.com")       

        db.session.add(usuario)
        db.session.commit()
        print(f'Base de datos creada y poblada')




if __name__ == '__main__':
    app.run(debug=True)

