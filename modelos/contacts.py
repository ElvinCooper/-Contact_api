from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db  = SQLAlchemy()

class Contacto(db.Model):
    __tablename__ = 'mis_contactos'
    
    id     = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email  = Column(String, nullable=False)

    
    def __repr__(self):
        return f"<Contact {self.name}>"