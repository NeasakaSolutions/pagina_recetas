# Importaciones
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # Es la pagina principal de Django y no puede ser modificada
    path('admin/', admin.site.urls),
    # Ruta principal creada por nosotros
    path('', include('home.urls')),
]
