# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from recetas.serializers import RecetaSerializer
from recetas.models import Receta

# Clase para busquedas grupales
class Clase1(APIView):

    def get (self, request):

        # Listar todos los id ordenados de mayor a menor
        data = Receta.objects.order_by('-id').all()
        datos_json = RecetaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data})
