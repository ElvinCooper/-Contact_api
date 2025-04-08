import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Ruta absoluta al archivo SQLite
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'mis_contactos.db')}"
    
    # Desactiva el seguimiento de modificaciones de objetos para ahorrar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para sesiones, JWT etc..
    SECRET_KEY = os.environ.get("SECRET_KEY", "12345cooper")
