# Importaciones
from django.urls import path
from recetas.views import Clase1

urlpatterns = [
    path('recetas', Clase1.as_view()),
]
