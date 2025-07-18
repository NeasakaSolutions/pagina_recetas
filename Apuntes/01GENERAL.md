---
marp: true
theme: uncover
paginate: true
class: lead
---

# Tutorial del como se realizo este proyecto
### NOTAS al final de la presentacion

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
- django rest framework **(Pag. 15)**
- mySQL client **(Pag. 17)**
- dotenv **(Pag. 20)**
- django-autoslug **(Pag.28)**
---

- insomnia

---

### Crear el entorno virtual:

- Dirigirse a la carpeta principal del proyecto, en este caso la ruta es la siguiente:

```bash
D:\pagina_recetas>
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
# Notas:
- Cada .gitignore debera de contener:

``` bash
entorno
.env
__init__.py
__pycache__
*pyc
```
---

