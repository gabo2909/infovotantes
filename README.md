# Prueba de desarrollo backend

### OBJETIVO

Se requiere hacer un sistema de información para registrar los datos de los votantes de los distintos municipios de Colombia.

* Validar sesiones a través de un token, el cual es consumido por los demás servicios
* Gestión de roles de usuario (PERMISOS)

### PREVIO A LA INSTALACIÓN

* Cargar el backup de la base de datos proporcionado junto con el proyecto

```
# Instalar unaccent extension - PostgreSQL

CREATE EXTENSION unaccent;
```

### INSTALACIÓN

```
# Crear un entorno virtual
python -m venv "virtualenv_name"

# Instalar librerías y dependencias
pip install -r requirements.txt

# Iniciar el proyecto
python manage.py runserver
```

### REQUERIMIENTOS

* [Python 3.x](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
