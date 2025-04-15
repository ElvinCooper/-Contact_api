# 📇 API REST - Contactos

Una API RESTful para gestionar contactos, desarrollada con **Flask**, **JWT**, **SQLAlchemy**, **Swagger** y más.

---

## 🚀 Funcionalidades principales

- Registro y login de usuarios con tokens JWT
- Gestión de contactos (crear, listar, actualizar, eliminar)
- Protección de rutas con autenticación
- Documentación interactiva con Swagger
- Envío de correos al registrarse o iniciar sesión (Mailgun, opcional)
- Estructura profesional usando Blueprints y Marshmallow
- Pruebas automatizadas con Pytest

---

## 🛠️ Instalación local

### 1. Clona el proyecto

```bash
git clone https://github.com/ElvinCooper/-Contact_api.git
cd tu-repo
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crea el archivo `.env`

```env
JWT_SECRET_KEY=tu_clave_secreta
MAILGUN_API_KEY=tu_api_key_mailgun
MAILGUN_DOMAIN=sandboxXXXX.mailgun.org
MAILGUN_FROM=Mailgun Sandbox <postmaster@sandboxXXXX.mailgun.org>
```

> ⚠️ Si no usarás correos, puedes dejar los campos vacíos temporalmente.

---

## 🗃️ Base de datos

### Iniciar migraciones

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

### Crear la base de datos (opcional comando extra)

```bash
flask db_create
```

---

## ▶️ Ejecutar el servidor

```bash
flask run --debug  # Esto activa el servidor en modo debuging para desarrllo 
```

---

## 🔐 Rutas protegidas con JWT

Para acceder a las rutas privadas:

1. Regístrate en `/api/register`
2. Haz login en `/api/login` y copia el token
3. En Swagger UI haz clic en `Authorize` y pega:

```
Bearer (espacio) + (tu token)  
```

---

## 📚 Documentación Swagger

Accede a la documentación interactiva en:

```
http://localhost:5000/apidocs
```

Desde ahí puedes probar todos los endpoints directamente.

---

## 🧪 Pruebas con Pytest

```bash
pytest -v
```

> Las pruebas usan una base de datos en memoria (`sqlite:///:memory:`).

---

## 🗂 Estructura del proyecto

```
/proyecto_api_contact/
├── app.py
├── config.py
├── extensions.py
├── /modelos/
├── /routes/
├── /schemas/
├── /templates/
├── /tests/
├── migrations/
├── .env
└── requirements.txt
```

---

## 📦 Requisitos

- Python 3.11+
- pip
- SQLite (o configurar tu propio motor SQL)

---

## 🧑‍💻 Contribuciones

¡Toda contribución es bienvenida!  
Puedes abrir issues o pull requests si deseas proponer mejoras, reportar bugs o aportar con nuevas funciones.

---

## 📜 Licencia

MIT License
```
