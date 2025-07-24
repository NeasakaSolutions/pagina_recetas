# Importaciones
from django.urls import path
from seguridad.views import Clase1
from seguridad.views import Clase2

# Direcciones
urlpatterns = [
    path('seguridad/registro', Clase1.as_view()),
    path('seguridad/verificacion/<str:token>', Clase2.as_view()),
]
