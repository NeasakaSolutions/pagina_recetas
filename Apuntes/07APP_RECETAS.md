---
marp: true
theme: uncover
paginate: true
class: lead
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

- En la "Clase2" de la app recetas se agregara el metodo delete:

```python
def delete(self, request, id):
        try:
            data = Receta.objects.filter(id = id).get()
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "La receta que se intenta eliminar no existe"}, 
                                status = HTTPStatus.NOT_FOUND)
        
        os.remove(f"./uploads/recetas/{data.foto}")
        Receta.objects.filter(id = id).delete()
        return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro"}, 
                            status = HTTPStatus.OK)
```
---
- En views.py de la app categorias modificar el metodo delete:

```python
    def delete(self, request, id):
        try:
            data = Categoria.objects.filter(pk = id).get()
        except Categoria.DoesNotExist:
            raise Http404
        if Receta.objects.filter(categoria_id = id).exists():
            return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado"}, 
                                status = HTTPStatus.BAD_REQUEST)
        Categoria.objects.filter(pk = id).delete()
        return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro correctamente"},
                            status = HTTPStatus.OK)
```