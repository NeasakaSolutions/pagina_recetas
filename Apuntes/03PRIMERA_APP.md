---
marp: true
theme: uncover
paginate: true
class: lead
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