# Importaciones
from django.urls import path
from .views import Clase1

urlpatterns = [
    path('categorias', Clase1.as_view())
]


