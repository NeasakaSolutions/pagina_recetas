---
marp: true
theme: uncover
paginate: true
class: lead
---
### App de contactos

- Generar la app

```python
django-admin startapp contacto
```

- Generar el archivo urls.py en la app de contacto:

```python
from django.urls import path
from contacto.views import Clase1

urlpatterns = [
    path('contacto', Clase1.as_view()),
]
```
---

- Registrar la app contaco en la url principal:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/v1/', include('categorias.urls')),
    path('api/v1/', include('recetas.urls')),
    path('api/v1/', include('contacto.urls')),
]
```

- Crear la nueva url en insomina

---
- En views.py de la app contacto:
```python
# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from categorias.models import Categoria
from recetas.models import Receta


class Clase1(APIView):

    def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio."})
        if request.data.get("correo") == None or not request.data["correo"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio."})
        if request.data.get("telefono") == None or not request.data["telefono"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo telefono es obligatorio."})
        if request.data.get("mensaje") == None or not request.data["mensaje"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo mensaje es obligatorio."})
```
---
- En settings.py agregar la app contacto

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
    'contacto',
]
```

---
- En models.py de la app contacto

```python
from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length = 100, blank = True, null = True)
    correo = models.CharField(max_length = 100, blank = True, null = True)
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    mensaje = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = "Contactos"
```

---

- Generar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

- En views.py de la app contacto agregar dentro de la funcion post:

```python
try:
    Contacto.objects.create(nombre = request.data['nombre'], correo = request.data['correo'], 
                        telefono = request.data['telefono'], mensaje = request.data['mensaje'], 
                        fecha = datetime.now())
except Exception as e:
    return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado"}, 
                        status = HTTPStatus.BAD_REQUEST)
        
    return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro exitosamente"}, 
                        status = HTTPStatus.OK)
```
---
- Crear una carpeta de utilidades en la raiz del proyecto, generar en la carpeta un archivo "__init__.py" y otro "utilidades.py"

- Importar el archivo utilidades en views.py de contactos:

```python
from utilidades.utilidades import utilidades
```

- Crear una cuenta en mailtrap

- En imboxes registrar los datos que nos dan en el .env

```bash
SMTP_SERVER=xxxxx.xxxx.xxxxx.xx
SMTP_PORT=587
SMTP_USER=xxxxxxxxxx
SMTP_PASSWORD=xxxxxxxxxxx
```
---
- En utilidades.py:

```python
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPResponseException

def sendMail(html, asunto, para):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = para
    msg.attach(MIMEText(html, 'html'))

    try:
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(os.getenv("SMTP_USER"), para, msg.as_string())
        server.quit()
    except SMTPResponseException as e:
        print("Error envio mail")
```
---
- En views.py de la app contacto, antes del retorno principal, agregar:

```python
html = f"""
        <h1>Nuevo mensaje de sitio web</h1>
        <ul>
            <li>Nombre: {request.data['nombre']}</li>
            <li>Correo: {request.data['correo']}</li>
            <li>Telefono: {request.data['telefono']}</li>
            <li>Mensaje: {request.data['mensaje']}</li>
        </ul>
"""
utilidades.sendMail(html, "Prueba de correo", request.data['correo'])
```
