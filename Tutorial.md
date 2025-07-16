---
marp: true
theme: uncover
paginate: true
class: lead
---

# Tutorial del como se realizo este proyecto
### NOTAS al final de la presentacion

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
- En views.py de la app categorias, importar:
```python
from django.utils.text import slugify
```

- Crear la funcion de put en **"Clase2"**:

```python
def put(self, request, id):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        
        try:
            data = Categoria.objects.filter(pk = id).get()
            Categoria.objects.filter(pk = id).update(nombre = request.data.get("nombre"),
                                    slug = slugify(request.data.get("nombre")))
            return JsonResponse({"estado": "ok", "mensaje": "Se modifico el registro correctamente"},
                                 status = HTTPStatus.OK)

        except Categoria.DoesNotExist:
            raise Http404
```
---
- Probar en insomnia con la funcion PUT en una registro, en este caso la url fue:
```bash
http://xxx.x.x.x:xxxx/api/v1/categorias/5
```

- Se agrego un json en insomnia:

```python
{
    "nombre": "Ensaladas frescas"
}
```
---
- En views.py de la app categoria agregar la funcion para eliminar un registro en la **"Clase2"**:

```python
def delete(self, request, id):
         
    try:
            # Busca el registro
        data = Categoria.objects.filter(pk = id).get()
            # Eliminar en caso de que si encuentre el registro
        Categoria.objects.filter(pk = id).delete()
            # Retorno
        return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro correctamente"},
                                 status = HTTPStatus.OK)

    except Categoria.DoesNotExist:
        raise Http404
```
---
### Configuracion de la app recetas

- Crear la nueva aplicacion:

```bash
django-admin startapp recetas
```

- En la app recetas, crear un archivo urls.py con el siguiente contenido:

``` python
from django.urls import path
from recetas.views import Clase1

urlpatterns = [
    path('recetas', Clase1.as_view()),
]
```
---

- En el proyecto principal (backend), agregar la siguiente ruta en urls.py:

```python
path('api/v1/', include('recetas.urls')),
```

- En views.py de la app recetas, agregar:

```python
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

class Clase1(APIView):

    def get (self, request):
        pass
```
---
- En settings.py agregar en INSTALLED_APPS, la app de recetas:

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
    'recetas',
]
```
---
- En models de la app recetas:

```python
from django.db import models
from autoslug import AutoSlugField
from categorias.models import Categoria

class Receta(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, default = 1)
    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre', max_length = 100)
    tiempo = models.CharField(max_length = 100, null = True)
    foto = models.CharField(max_length = 100, null = True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now = True)
```
---
- Crear las migraciones por medio de consola:

```bash
python manage.py makemigrations # 1er ejecucion
python manage.py migrate # 2da ejecucion

```
- Crear el archivo serializers.py para la app recetas y agregar:

```python
from rest_framework import serializers
from recetas.models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receta
        fields = ('__all__')
```
---
- Llenar la tabla con registros

``` bash
INSERT INTO `django_recetas`.`recetas` (`id`, `nombre`, `slug`, `tiempo`, `foto`, `descripcion`, `fecha`, `categoria_id`) VALUES ('1', 'Pastel de maiz', 'pastel-de-maiz', '2 horas', 'Furina.png', 'Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales', '2024-09-13 00:00:00.000000', '1');
INSERT INTO `django_recetas`.`recetas` (`id`, `nombre`, `slug`, `tiempo`, `foto`, `descripcion`, `fecha`, `categoria_id`) VALUES ('2', 'Pozole mexicano', 'pozole-mexicano', '1 hora y media', 'Furina.png', 'Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales', '2024-09-13 00:00:00.000000', '1');
INSERT INTO `django_recetas`.`recetas` (`id`, `nombre`, `slug`, `tiempo`, `foto`, `descripcion`, `fecha`, `categoria_id`) VALUES ('3', 'Pastel de uwu', 'pastel-de-uwu', 'una hora', 'Furina.png', 'Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales', '2024-09-13 00:00:00.000000', '4');
INSERT INTO `django_recetas`.`recetas` (`id`, `nombre`, `slug`, `tiempo`, `foto`, `descripcion`, `fecha`, `categoria_id`) VALUES ('4', 'Vodka tonica', 'vodka-tonica', '2 minutos', 'Furina.png', 'Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales', '2024-09-13 00:00:00.000000', '3');
```

- En views.py de la app receta importar:

```python
from recetas.serializers import RecetaSerializer
from recetas.models import Receta
```

---

- En views.py de la app recetas completar la funcion que se tiene:

```python
class Clase1(APIView):

    def get (self, request):
        data = Receta.objects.order_by('-id').all()
        datos_json = RecetaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data})
```

- Crear una nueva ruta en insomnia:

```bash
http://xxx.x.x.x:xxxx/api/v1/categorias
```

---

- En serializers.py de la app recetas:

```python
from rest_framework import serializers
from recetas.models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source = "categoria.nombre")
    fecha = serializers.DateTimeField(format = "%d/%m/%Y")

    class Meta:
        model = Receta
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id", "imagen")
```

- En archivo .env, agregar tu direccion ip de django en base_url

```bash
BASE_URL = http://xxx.x.x.x:xxxx/
```
---
- En el archivo serializers.py de la app recetas, agregar:

```python
    def get_imagen(self, obj):
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"
```
- En urls.py de la app recetas agregar la ruta:

```python
path('recetas/<int:id>', Clase2.as_view())
```

- En views.py de la app recetas agregar las siguientes importaciones:

```python
import os
from dotenv import load_dotenv
from django.utils.dateformat import DateFormat
```
---
- En views.py de la app recetas agregar esta clase:

```python
class Clase2(APIView):

    def get(self, request, id):
        try:
            data = Receta.objects.filter(id = id).get()
            return JsonResponse({"data": {"id" : data.id, "nombre": data.nombre, "slug": data.slug, 
                                "tiempo": data.tiempo, "descripcion": data.descripcion, 
                                "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id, 
                                "categoria" : data.categoria.nombre, 
                                "imagen": f"{os.getenv("BASE_URL")}uploads/recetas/{data.foto}"}}, 
                                status = HTTPStatus.OK)
        except Receta.DoesNotExist:
            raise Http404
```

- En insomina, seleccionar el metodo post para recetas y cambiar a body -> "Form Data" y almacenar los datos que pide la BD (nombre, tiempo, descripcion, categoria_id)

---

- En views.py de la app recetas, agregar la nueva importacion:

```python
from categorias.models import Categoria
from datetime import datetime
```

- Agregar el metodo post en la Clase1

```python
    def post(self, request):
        try:
            Receta.objects.create(nombre = request.data["nombre"], tiempo = request.data.get("tiempo"),
                                  descripcion = request.data["descripcion"], categoria_id = request.data.get("categoria_id"), 
                                  fecha = datetime.now(), foto = "sss")
            return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente"}, 
                                status = HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
```

- En insomnia probar el metodo post y verificar en la BD

---

- Agregar las validaciones en la funcion post de la app recetas:

```python
# Validacion del nombre
if request.data.get("nombre") == None or not request.data["nombre"]:
    return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
# Validacion del tiempo
if request.data.get("tiempo") == None or not request.data["tiempo"]:
    return JsonResponse({"estado": "error", "mensaje": "El campo tiempo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
# Validacion de la descripcion:
if request.data.get("descripcion") == None or not request.data["descripcion"]:
    return JsonResponse({"estado": "error", "mensaje": "El campo descripcion es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
# Validacion de la categoria_id:
if request.data.get("categoria_id") == None or not request.data["categoria_id"]:
    return JsonResponse({"estado": "error", "mensaje": "El campo categoria es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
```
---
- Validacion para no repetir el nombre en la BD, se agrega abajo de las otras validaciones:

```python
if Receta.objects.filter(nombre = request.data.get("nombre")).exists():
    return JsonResponse({"estado": "error", "mensaje": f"El nombre {request.data["nombre"]} no esta disponible"}, 
                        status = HTTPStatus.BAD_REQUEST)
```

- Validacion para verificar que el campo de categorias exista:
```python
try:
    categoria = Categoria.objects.filter(pk = request.data["categoria_id"]).get()
except Categoria.DoesNotExist:
    return JsonResponse({"estado": "error", "mensaje": "La categoria no existe en la base de datos."}, 
                        status = HTTPStatus.BAD_REQUEST)
```
---
- En views.py de la app recetas agregar la importacion:

```python
from django.core.files.storage import FileSystemStorage
```

- Buscar donde se encuentra la variable foto = "foto" y cambiar a foto = foto:

```python
Receta.objects.create(nombre = request.data["nombre"], tiempo = request.data.get("tiempo"),
                                  descripcion = request.data["descripcion"], categoria_id = request.data.get("categoria_id"), 
                                  fecha = datetime.now(), foto = foto)
```

- En insomnia, con el metodo post en recetas, adjuntar un nuevo campo para la foto de tipo file y subir una foto.
---
- Configuracion para subir una imagen, se coloca en la funcion post de Clase1 en views.py de la app recetas:

```python
fs = FileSystemStorage()
try:
    foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
except Exception as e:
    return JsonResponse({"estado": "error", "mensaje": "Debe de adjuntar una foto en el campo foto"}, 
                        status = HTTPStatus.BAD_REQUEST)
        
try:
    fs.save(f"recetas/{foto}", request.FILES['foto'])
    fs.url(request.FILES['foto'])
except Exception as e:
    return JsonResponse({"estado": "error", "mensaje": "Se produjo un error al intentar subir el archivo"}, 
                        status = HTTPStatus.BAD_REQUEST)
```
---
### MIME types
- Agregar la validacion de MIME en el post de la app recetas antes del codigo de subir la imagen y encapsular lo demas de la foto en la condicional:

```python
if request.FILES["foto"].content_type == "image/jpeg" or request.FILES["foto"].content_type == "image/png":
```
---
# Notas:
- Cada .gitignore debera de contener:

``` bash
entorno
.env
__init__.py
__pycache__
*pyc
```
---

