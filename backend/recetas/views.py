# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from recetas.serializers import RecetaSerializer
from recetas.models import Receta
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os

# Clase para busquedas grupales
class Clase1(APIView):

    def get (self, request):

        # Listar todos los id ordenados de mayor a menor
        data = Receta.objects.order_by('-id').all()
        datos_json = RecetaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data})
    
# Clase para busqueda individual:
class Clase2(APIView):

    def get(self, request, id):
        try:
            data = Receta.objects.filter(id = id).get()
            return JsonResponse({"data": {"id" : data.id, "nombre": data.nombre, "slug": data.slug, 
                                "tiempo": data.tiempo, "descripcion": data.descripcion, 
                                "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id, 
                                "categoria" : data.categoria.nombre, 
                                "imagen": f"{os.getenv("BASE_URL")}uploads/recetas/{data.foto}"}}, 
                                status = HTTPStatus.OK)
        except Receta.DoesNotExist:
            raise Http404
