---
marp: true
theme: uncover
paginate: true
class: lead
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