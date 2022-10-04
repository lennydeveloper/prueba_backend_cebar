# Prueba Backend CEBAR

El objetivo de este proyecto es desarrollar el test de desarrollo backend para CEBAR SAS

### Requerimientos del sistema

* CRUD para cada modelo
* Gestión de departamentos, municipios y mesas de votación
* Cantidad total de votantes inscritos por líder.
* Cantidad total de votantes en el sistema
* Cantidad total de votantes inscritos por municipio
* Cantidad total de votantes inscritos por mesa de votación

NOTA: El sistema en general opera con la estructura API REST mediante un JSON, sin embargo se trabajó con un multipart/form-data para registro de usuario permitiendo así la carga de imagen para el usuario correspondiente

### Validación de token en los servicios (JSON Web Token)

Para este requerimiento en específico se trabajó con un JWT para autenticación de usuario con persistencia de datos, el cual almacena la información de inicio de sesión. Los servicios creados en este proyecto consumen la información de este token para poder operar correctamente.

### Validaciones a través del formulario

Se requería realizar validaciones mediante un formulario para registrar votantes. El formulario se puede ubicar a través del django admin. La validación que se realizó para cumplir con este item fue para el campo cédula, validando tamaño de este campo y evitando registros duplicados
```
<context>:8000/admin/registraduria/votante/add/

http://localhost:8000/admin/registraduria/votante/add/
```

### Diagrama entidad-relación

Este diagrama lo pueden encontrar en la ruta
```
sources/cebar_mer.png
```

### Colección de pruebas (Postman)

La colección de pruebas desarrollado para validar el correcto funcionamiento del API lo pueden encontrar en la ruta
```
sources/prueba_cebar_backend.postman_collection.json
```

### Ejecutar el proyecto

El archivo de configuración del proyecto se encuentra en
```
backend/settings.py
```

Comandos requeridos
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

El respaldo de la BD y demás Scripts se podrán encontrar en la carpeta sources

### Requerimientos
* Python 3.x
* Virtualenv

### Librerías

Las librerías empleadas en este desarrollo se puede encontrar en el archivo requirements.txt

### Crear el entorno virtual

```bash
$ python -m venv [nombre del virtualenv]
$ source Scripts/activate
$ pip install -r requirements.txt
```