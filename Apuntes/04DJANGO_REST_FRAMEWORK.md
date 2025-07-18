---
marp: true
theme: uncover
paginate: true
class: lead
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