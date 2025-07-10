# Importaciones
from django.urls import path
from home.views import home_inicio

urlpatterns = [
    # Cuando las comillas estan vacias significa que se inicia la ruta principal
    path('', home_inicio), # Se llama a la funcion home_inicio
]
