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
- en views.py de la app
---