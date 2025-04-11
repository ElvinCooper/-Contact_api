from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
import uuid
from extensions import db

class Contacto(db.Model):
    __tablename__ = 'mis_contactos'
    
    id             = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre         = db.Column(db.String(100), nullable=False)
    email          = db.Column(db.String(120), nullable=False)
    telefono       = db.Column(db.String(20))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)

    
    def __repr__(self):
        return f"<Contact {self.name}>"