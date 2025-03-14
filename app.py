from flask import Flask
import sqlite3

app = Flask(__name__)

# contactos = [
#              (10, 'jose', 'jose@gmail.com'),
#              (11, 'miguel', 'miguel03@gmail.com'),
#              (12, 'mariana', 'mariana14@gmail.com')
#              ]

@app.route('/')
def get_contactos():
    records = 0
    conn = sqlite3.connect('api_contacts.db')
    cursor = conn.cursor()
    cursor.execute("select id, nombre, email from contacts")
    query = cursor.fetchall()
    for datos in query:
        print(datos)
        records += 1
    
    conn.close()
    print(f"Cantidad de registros: {records}")
    return query


    




if app == '__main__':
    app.run(debug=True)