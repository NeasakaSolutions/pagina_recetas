# Importaciones
from rest_framework import serializers
from recetas.models import Receta
from dotenv import load_dotenv
import os

class RecetaSerializer(serializers.ModelSerializer):
    
    # Muestra el valor del campo que se encuentra en la tabla y no solo el llave foranea
    categoria = serializers.ReadOnlyField(source = "categoria.nombre")
    #categoria = serializers.CharField(source = "categoria.nombre")
    fecha = serializers.DateTimeField(format = "%d/%m/%Y") # 13/10/2025
    # Creamos el campo para la funcion
    imagen = serializers.SerializerMethodField()

    class Meta:
        # Modelo que se usara
        model = Receta
        # Datos que consultaran
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id", 
                "imagen")

    # Funcion para el formateo de la imagen
    def get_imagen(self, obj):

        #return f"Hola Mundo {obj.id}"
        #return(os.getenv("settings.BASE_URL"))
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"

