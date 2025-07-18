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
- En views.py de la app seguridad
```python
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
```
---