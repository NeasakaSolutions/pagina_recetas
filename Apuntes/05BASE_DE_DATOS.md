---
marp: true
theme: uncover
paginate: true
class: lead
---
### Base de datos

- Crear una base de datos, en este caso nuestra bd se llama **"django_recetas"**

- Para instalar mySQL client en linux se utiliza lo siguiente:

```bash
apt-get install python-dev default-libmysqlclient-dev
```

- Instalar para hacer la conexion con mySQL en la app: **(Recuerda activar el entorno y estar en la ruta del proyecto principal)**

```bash
pip install mysqlclient
```

---

- Empezar a generar el requirements, se pone en terminal:

```bash
pip freeze
```

- Crear un archivo nuevo llamado "requirements.txt" y pegra lo que dio la terminal:

```python
Django==5.2.4
djangorestframework==3.16.0
mysqlclient==2.2.7
```

- Para instalar los archivos de requirements.txt se ejecuta en terminal lo siguiente:

``` bash
pip installrequirements.txt
```
---
### Configuaracion de la bd

- En settings.py modificar la parte de DATABASES:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
```
---
- Instalar dotenv, en terminal ejecutar:
```bash
pip install python-dotenv
```

- Crear un archivo .env y llenar la siguiente informacion:

```bash
DATABASE_SERVER = server
DATABASE_USER = root
DATABASE_PASSWORD = ijole123
DATABASE_PORT = 3306
DATABASE_BD = nombre_de_la_bd
```
---
- Crear un archivo .env.example y poner lo mismo que en .env pero sin valores:

```bash
DATABASE_SERVER =
DATABASE_USER =
DATABASE_PASSWORD =
DATABASE_PORT =
DATABASE_BD =
```

- Crear un .gitignore y agregar el .env

- En settings.py agregar las siguientes importaciones:

```python
import os
from dotenv import load_dotenv
```
---
- En settings.py agregar la siguiente funcion:

``` python
load_dotenv()
```

- Modificar tu seccion de DATABASES con dotenv:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_BD'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_SERVER'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': {
            'autocommit': True
        }
    }
}
```
---

- En settings.py, cambiar el valor de la variable debug porque ya se esta trabajando con mySQL:

```python
DEBUG = os.getenv('DEBUG')
```

- Se crea una nueva aplicacion, en este caso bajo el nombre de "categorias"

```bash
django-admin startapp categorias
```
---
- En urls.py de backend agregar las siguientes importaciones y nueva variable:

```python
from django.conf import settings
from django.conf import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

- En el mismo archivo, agregar la ruta de la nueva app:

```python
path('api/v1/', include('categorias.urls')),
```