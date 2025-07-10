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
- django rest framework **(Pag 15)**

---
---

### Crear el entorno virtual:

- Dirigirse a la carpeta principal del proyecto, en este caso la ruta es la siguiente:

```bash
D:\CURSOS\django\pagina_recetas>
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
(entorno) D:\CURSOS\django\pagina_recetas>
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



---