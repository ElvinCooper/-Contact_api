from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
import uuid
from extensions import db

class Contacto(db.Model):
    __tablename__ = 'mis_contactos'
    
    #id     = Column(Integer, primary_key=True) 
    id     = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    email  = db.Column(db.String(120), nullable=False)

    
    def __repr__(self):
        return f"<Contact {self.name}>"