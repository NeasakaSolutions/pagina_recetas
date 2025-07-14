# Importaciones
from rest_framework import serializers
from recetas.models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    
    # Muestra el valor del campo que se encuentra en la tabla y no solo el llave foranea
    categoria = serializers.ReadOnlyField(source = "categoria.nombre")
    #categoria = serializers.CharField(source = "categoria.nombre")
    fecha = serializers.DateTimeField(format = "%d/%m/%Y") # 13/10/2025

    class Meta:
        # Modelo que se usara
        model = Receta
        # Datos que consultaran
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id")
