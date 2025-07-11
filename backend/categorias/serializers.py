# Importaciones
from rest_framework import serializers
from categorias.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Modelo que se usara
        model = Categoria
        # Datos que consultaran
        fields = ("id", "nombre", "slug")
        # fields = '__all__' # Es lo mismo que arriba
        # fields = ('__all__') # Es lo mismo que arriba

