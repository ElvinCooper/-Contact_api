from flask import Flask, request, jsonify
import re, os
import sqlite3, requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mis_contactos.db')


db  = SQLAlchemy(app)



class Contacto(db.Model):
    __tablename__ = 'mis_contactos'
    id     = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email  = Column(String, nullable=False)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Base de datos creada exitosamente !')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Base de datos eliminada')


# Definicion de los datos a partir del modelo Contacto

@app.cli.command('db.seed')
def db_seed():
    contacto1 = Contacto(id=None,
                         nombre='Andrew',
                         email='andrew@gmail.com')
    
    contacto2 = Contacto(id=None,
                         nombre='Elvin',
                         email='elvin@gmail.com')
    
    contacto3 = Contacto(id=None,
                         nombre='Katherin',
                         email='katherin@gmail.com')

    db.session.add(contacto1)
    db.session.add(contacto2)
    db.session.add(contacto3)

    db.session.commit()
    print('Base de datos poblada')


if __name__ == '__main__':
    app.run(debug=True)