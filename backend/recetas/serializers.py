# Importaciones
from rest_framework import serializers
from recetas.models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Modelo que se usara
        model = Receta
        # Datos que consultaran
        fields = ('__all__')
