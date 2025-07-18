# Importaciones
from django.urls import path
from seguridad.views import Clase1

# Direcciones
urlpatterns = [
    path('seguridad/registro', Clase1.as_view()),
]
