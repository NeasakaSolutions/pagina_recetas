---
marp: true
theme: uncover
paginate: true
class: lead
---
### Seguridad en las rutas
- Crear una nueva app
```bash
django-admin startapp seguridad
```

- Crear el archivo urls.py en la app de seguridad
```python
from django.urls import path
from seguridad.views import Clase1

urlpatterns = [
    path('seguridad/registro', Clase1.as_view()),
]
```
---
- Agregar la url de seguridad en las urls.py principales (Raiz del proyecto)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/v1/', include('categorias.urls')),
    path('api/v1/', include('recetas.urls')),
    path('api/v1/', include('contacto.urls')),
    path('api/v1/', include('seguridad.urls')),
]
```
---
- En views.py de la app seguridad
```python
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus

class Clase1(APIView):
    
    def post(self, request):
        pass
```
---
- Crear un nuevo super usuario:
```bash
python manage.py createsuperuser
```

- Generar datos para el acceso
```bash
User: yo@neasakapendragon.com
Email: yo@neasakapendragon.com
Password: 12345678
```

- Verificar la creacion del usuario en la bd en la tabla auth_user

- En settings.py agregar en INSTALLED_APPS la app de seguridad
---

- Generamos un token en la app de seguridad en models.py:
```python
from django.db import models
from django.contrib.auth.models import User

class UserMetadata(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    token = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return f"{self.first_user} {self.last_name}"
    
    class Meta:
        db_table = 'users_metadata'
        verbose_name = "User metadata"
        verbose_name_plural = "User metadata"
```
---

- Aplicamos las migraciones correspondientes:

```bash
python manage.py makemigrations
python manage.py migrate
```

- Verificar que exista la nueva tabla y hacer un registro:

``` bash
SELECT * FROM users_metadata;
```
---
- Agregar las validaciones en views.py de la app seguridad

```python
if request.data.get("nombre") == None or not request.data.get("nombre"):
    return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, 
                        status = HTTPStatus.BAD_REQUEST)
if request.data.get("correo") == None or not request.data.get("correo"):
    return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio"}, 
                        status = HTTPStatus.BAD_REQUEST)
if request.data.get("password") == None or not request.data.get("password"):
    return JsonResponse({"estado": "error", "mensaje": "El campo password es obligatorio"}, 
                        status = HTTPStatus.BAD_REQUEST)
if User.objects.filter(email = request.data["correo"]).exists():
    return JsonResponse({"estado": "error", "mensaje": f"El correo {request.data["correo"]} ya existe."}, 
                        status = HTTPStatus.BAD_REQUEST)
```
---
- Crear una nueva request en insomnia:

```bash
http://xxx.x.x.x:xxxx/api/v1/contacto
```

- Mandar un json

```python
{
    "nombre" : "Ijole",
    "correo" : "nombre@correo.com",
    "password" : "123456"
}
```
---
- Agregar la creacion dl usuario:
```python
token = uuid.uuid4()
 url = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}"
    try:
        u = User.objects.create_user(username = request.data["correo"], password = request.data["password"], 
                                    email = request.data["correo"], first_name = request.data["nombre"], 
                                    last_name = "", is_active = 0)
            
        UsersMetadata.objects.create(token = token, user_id = u.id)
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado."}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente."}, 
                                status = HTTPStatus.CREATED)
```
---
- Agregar respuesta en las validaciones:

```python
html = f"""
    <h3>Verificacion de cuenta</h3>
    Hola {request.data["nombre"]} te haz registrado exitosamente. Para activar tu cuenta haz click en 
    el siguiente enlace: <br/>
    <a href="{url}">{url}</a>
    <br/>
    O copia y pega la siguiente url en tu navegador favorito:
    <br/>
    {url}
    """
utilidades.sendMail(html, "Verificacion", request.data["correo"])
```
- En urls.py de la app seguridad agregar la ruta de verificacion:
```python
path('seguridad/verificacion/<str:token>', Clase2.as_view()),
```
---
- En .env del fronted: (la url es la misma que BASE_URL, solo cambia el puerto)
```bash
BASE_URL_FRONTED=http://xxx.x.x.x:5173/login
```

- En views.py de la app seguridad agregar la Clase2:
```python
class Clase2(APIView):

    def get(self, request, token):
        
        if token == None or not token:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, 
                                status = 404)
        try:
            data = UsersMetadata.objects.filter(token = token).filter(user__is_active = 0).get()
            UsersMetadata.objects.filter(token = token).update(token = "")
            User.objects.filter(id = data.user_id).update(is_active = 1)
            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTED"))
        except UsersMetadata.DoesNotExist:
            raise Http404
```
---
- Craer una nueva ruta en insmonia:
```bash
http://xxx.x.x.x:xxxx/api/v1/seguridad/login
```

- Crear el endpoint con el metodo post en insomnia:
```bash
{
	"correo": "yo@neasakapendragon",
	"password": "12345678"
}
```

- Agregar la nueva ruta en urls.py de la app s3eguridad:
```python
path('seguridad/login', Clase3.as_view()),
```
---
- Se agrega la clase 3:
```python
class Clase3(APIView):

    def post(self, request):

        if request.data.get("correo") == None or not request.data.get("correo"):
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "mensaje": "El campo password es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        try:
            user = User.objects.filter(email = request.data["correo"]).get()
        except User.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "El correo ingresado no es valido."}, 
                                status = HTTPStatus.NOT_FOUND)
        

        auth = authenticate(request, username = request.data.get("correo"), password = request.data.get("password"))
        if auth is not None:
            pass
        else:
            return JsonResponse({"estado": "error", "mensaje": "La password ingresada no es valida."}, 
                                status = HTTPStatus.BAD_REQUEST)
```
---