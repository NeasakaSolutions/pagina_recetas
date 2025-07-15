# Importaciones
from django.urls import path
from recetas.views import Clase1
from recetas.views import Clase2

urlpatterns = [
    path('recetas', Clase1.as_view()),
    path('recetas/<int:id>', Clase2.as_view())
]
