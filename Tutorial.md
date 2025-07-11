---
marp: true
theme: uncover
paginate: true
class: lead
---

# Tutorial del como se realizo este proyecto

---

- Verificar librerias instaladas:

```bash
pip3 list # 1era forma de verificar
pip3 freeze # 2da forma de verificar
```
---

### Cosas necesarias:
En caso de no contar con alguna de las siguientes, se dejara la pagina en donde se muestra como se instala:
- python 3.10 en adelante.
- virtualenv **(Pag. 5)**
- django **(Pag. 7)**
- django rest framework **(Pag. 15)**
- mySQL client **(Pag. 17)**
- dotenv **(Pag. 20)**
- django-autoslug **(Pag.28)**
---

- insomnia

---

### Crear el entorno virtual:

- Dirigirse a la carpeta principal del proyecto, en este caso la ruta es la siguiente:

```bash
D:\pagina_recetas>
```

- Instalar el entorno virtualenv **(Verificar que no se tenga instalado)**

```bash
pip3 install virtualenv # Con python 3
pip install virtualenv # Versiones mas antiguas de python

```
---

- Generar el entorno virtual:

``` bash
virtualenv 
```

- Ponerle nombre al entorno:

``` bash 
virtualenv entorno
```

- Activar el entorno virtual **(Con el nombre de tu entorno)**:

``` bash
.\entorno\Scripts\activate # Windows
source/bin/activate # Linux
```

- Se generara una carpeta llamada entorno, apartir de ahora **no se le movera nada.**

---

### Instalacion de Django

- Activar el entorno virtual.

- Instalar Django en terminal:

```bash
pip install Django
```

- Verificar la instalacion:

```bash
pip list
```

---

- Debe mostrar Django en la lista:

```bash
Package  Version
-------- -------
asgiref  3.9.1
Django   5.2.4
pip      25.1.1
sqlparse 0.5.3
tzdata   2025.2
```

- Desinstalar Django, **no ejecutar**:

``` bash
pip uninstall Django
```
---

### Crear primer proyecto en Django

- Mostrar todos los comandos que ofrece Django:

```bash
django-admin # Arroja una lista de comandos
```

- Crear un **proyecto antes de la aplicacion**, en este caso se llamara backend:

```bash
django-admin startproject backend
```
---

### Estructura de un proyecto Django

```bash
manage.py   # Solo se invoca para generar comandos
asgi.py     # Son para configuraciones a nivel de aplicacion (asgi)
__init__.py # Indica a python que este directorio se debe de marcar como modulo
settings.py # Configuraciones generales
wsgi.py     # Despliega la aplicacion
urls.py     # Configuraciones de los enrutamientos generales
```

- Agregar lion en settings.py:

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_LI0N = True # Se afrega este
USE_TZ = True
```
---
- Asegurarse de estar en la carpeta del proyecto:

``` bash
(entorno) D:\pagina_recetas\backend>
```

- Ejecutar proyecto en django:

```bash
django-admin manage.py runserver # 1er forma, ya no se usa actualmente
python manage.py runserver       # 2da forma.
```

- La direccion que da, copiarla y ponerla en el navegador.

- En settings.py copiar tu ip en ALLOWED_HOSTS

```python
ALLOWED_HOSTS = ['xxx.x.x.x:xxxx']
```

---

### Crear primera aplicacion

- Borrar de tu proyecto el archivo **db.sqlite3** ya que no se usara.

- Ejecutar el sigueinte comando para generar la app principal (home).

``` bash
django-admin startapp home
```

---

- En views.py de la app home se genera una funcion para empezar a trabajar en la app:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home_inicio(request):
    return HttpResponse('<h1>Hola mundo desde Django</h1>')
```

- Dentro de la app home, se crea el archivo urls.py con el siguiente contenido:

```python
from django.urls import path
from home.views import home_inicio

urlpatterns = [
    path('', home_inicio), # Se importa el contenido de views.py
]
```
---

- Despues en urls.py del archivo principal (en este caso backend):

``` python
from django.contrib import admin
from django.urls import path
from django.urls import include # Se agrego esta importacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Ruta principal, por eso no se agrega nada en las comillas
]
```

- Prueba la app home

```bash
python manage.py runserver
```
---

### Instalar Django Rest Framework

- Ejecutar en terminal con el entorno activado y la carpeta del proyecto:

``` bash
pip install djangorestframework
```

- Recuerda validar tus librerias con:

``` bash
pip list
```

---
- En settings.py agregar rest_framework en INSTALLED APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```
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
---
### Configuracion de la app categorias

- Agregar la app en INSTALLED_APPS que se ubica en settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'categorias',
]
```
---
- En la app categorias se debera de crear un archivo urls.py y agregar lo siguiente:

```python
from django.urls import path
from .views import Clase1

urlpatterns = [
    path('categorias', Clase1.as_view())
]
```

---
- En views.py de la app categoria agregar el siguiente codigo:

```python
from rest_framework.views import APIView
from django.http.response import JsonResponse

# Clases de la aplicacion
class Clase1(APIView):

    # Funcion para mostrar datos
    def get(self, request):
        pass
```
---
### Crear modelo en app categoria

- Primero se debera de descargar django-autoslug:

```bash
pip install django-autoslug
```

- En el archivo models.py de la app categorias, generar las tablas

```python
from django.db import models
from autoslug import AutoSlugField

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre')
```
---

- Agregar debajo de todo el codigo de models.py en app categorias, **(opcional)**

```python
# Buenas practicas de programacion: (OPCIONAL)
def __str__(self):
    return self.nombre # Muestra el contenido del campo que se establezca
    
# Nombre que recibira la tabla en el administrador de django
class Meta:
    db_table = 'categorias'
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
```
---
### Crear migraciones

- Crear las tablas, aplicar en terminal:

```bash
python manage.py migrate
```

- Verificar que la base de datos se generen las tablas automaticamente.

- Crear la migracion de la app categorias.

```bash
python manage.py makemigrations
```

---

- Verificar en la carpeeta migrations que exista un archivo nuevo y contenga codigo.

- Una vez verificado, ejecutar:

```bash
python manage.py migrate
```
- Verificar que se haya creado la tabla de categorias en la base de datos
---
- Almacenar 4 registros en la tabla categorias:

```bash
INSERT INTO `django_recetas`.`categorias` (`id`, `nombre`, `slug`) VALUES ('1', 'Carnes y Pollos', 'carnes-y-pollos');
INSERT INTO `django_recetas`.`categorias` (`id`, `nombre`, `slug`) VALUES ('2', 'Pescados y mariscos', 'pescados-y-mariscos');
INSERT INTO `django_recetas`.`categorias` (`id`, `nombre`, `slug`) VALUES ('3', 'Tragos y cocteles', 'tragos-y-cocteles');
INSERT INTO `django_recetas`.`categorias` (`id`, `nombre`, `slug`) VALUES ('4', 'Frutas y verduras', 'frutas-y-verduras');
```

- En views.py de la app categorias agregar:

```python
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from categorias.models import Categoria 
from http import HTTPStatus

class Clase1(APIView):

    def get(self, request): 
        data = Categoria.objects.order_by('-id').all()
        return Response(data)
```
---

- En la app categorias crear un archivo llamado serializers.py y pegar:

```python
from rest_framework import serializers
from categorias.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ("id", "nombre", "slug")
```

- En la views.py de la app categorias agregar:

```python
from categorias.serializers import CategoriaSerializer
```
---

- Modificar la clase de categorias:

```python
class Clase1(APIView):

    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)
```
---
- En insomnia crear un nuevo proyecto y una nueva request con la direccion de tu localhost y la url:

```bash
http://xxx.x.x.x:xxxx/api/v1/categorias
```

- Usar el metodo GET y debera devolver los registros de la base de datos de la tabla categorias

- Crear una nueva ruta en urls.py de categorias y agregar una nueva importacion:

```python
from categorias.views import Clase2

path('categorias/<int:id>', Clase2.as_view()),
```
---

- En views.py de categorias crear una clase bajo el nombre de "Clase2" e importar nueva libreria:

```python
# Nueva importacion
from django.http import Http404

class Clase2(APIView):

    def get(self, request, id):
        try:
            data = Categoria.objects.filter(id = id).get()
            return JsonResponse({"data": {"id": data.id ,"nombre": data.nombre, "slug": data.slug}},
                             status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
```
---
- En views.py de la app categoria agregar la funcion post en **"Clase1"**:

```python
def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        try:
            Categoria.objects.create(nombre = request.data['nombre'])
            return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente"},
                                 status = HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
```
---
- Mandarle un json a la funcion post por medio de insomnia:

```python
{
    "nombre": "Categoria nueva"
}
```

- Verificar que todo funcione correctamente.
---


