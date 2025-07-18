---
marp: true
theme: uncover
paginate: true
class: lead
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