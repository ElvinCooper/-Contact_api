from flask import Flask, request
from flask import jsonify
import sqlite3

app = Flask(__name__)


# ENDPOINT PARA CONSULTAR LOS REGISTROS DE LA TABLA
@app.route('/contactos' , methods=['GET'])
def get_contactos():    
    try:
        with sqlite3.connect('api_contacts.db') as conn:
            conn.row_factory = sqlite3.Row # para convertir las filas en diccionarios
            cursor = conn.cursor()
            cursor.execute("select id, nombre, email from  CONTACTS")
            query = cursor.fetchall()

            if query:
                # convertir cada fila a un dicionario usando row_factory
                contactos = [dict(row) for row in query]
                
                for datos in query:
                    print(datos)                    
                                
                return jsonify(contactos)
            else:
                return jsonify({"mensaje": "No se encontraron registros."}), 400
            
    except sqlite3.Error as e:
        return jsonify({"Error": e}), 500


# ENDPOINT PARA CONSULTAR UN REGISTROS CON SU ID
@app.route('/consultar/<int:id>', methods=['GET'])
def consultar_contacto(id: int):
    try:
        with sqlite3.connect('api_contacts.db') as conn:
            conn.row_factory = sqlite3.Row # para convertir las filas en diccionarios
            cursor = conn.cursor()
            cursor.execute(f"select * from  CONTACTS WHERE ID ={id}")
            query = cursor.fetchall()

            if query:
                # convertir cada fila a un dicionario usando row_factory
                contactos = [dict(row) for row in query]
                
                return jsonify(contactos) 
            else:
                return jsonify({"mensaje": "No se encontraron registros con este id."}), 400
               
    except sqlite3.Error as e:
        return jsonify({"Error": e}), 500
    


# ENDPOINTS PARA INSERTAR UN NUEVO REGISTRO A LA TABLA CONTACTS
@app.route('/insert/<string:nombre>/<string:email>', methods=['POST'])
def insertar( nombre : str, email: str):
    try:             
        # validar si existe el nombre e email
        if not nombre or not email:
            return jsonify({"Error:": "Faltan parametros (nombre y email)"}), 400
        
        
        #conectando a la base de datos
        with sqlite3.connect('api_contacts.db') as conn:
            conn.row_factory = sqlite3.Row # para convertir las filas en diccionarios
            cursor = conn.cursor()

            #verificar si existe un contacto con el mismo email
            cursor.execute("SELECT 1 FROM CONTACTS WHERE email = ?", (email,))
            if cursor.fetchone() is not None:
                return jsonify({"Error": "Ya existe un usuario con ese email"}), 400
            
             # Insertar nuevo registro
            cursor.execute("INSERT INTO CONTACTS (nombre, email) VALUES (?, ?) ", (nombre, email))
            conn.commit() 

            #obtener nuevo id 
            nuevo_id = cursor.lastrowid

            return jsonify({
                "mensaje": "Contacto agregado correctamente",
                "id": nuevo_id,
                "nombre": nombre,
                "email": email
            }), 201          
               
    except sqlite3.OperationalError as e:
        return jsonify({"Error": str(e)}), 500

    except Exception as err:
        return jsonify({"Error": str(err)}), 500



if __name__ == '__main__':
    app.run(debug=True)