# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from categorias.serializers import CategoriaSerializer
from http import HTTPStatus
# Tabla que se usara para realizar las consultas
from categorias.models import Categoria 

# Clases de la aplicacion
class Clase1(APIView):

    # Funcion para mostrar datos
    def get(self, request):
 
        # SELECT * FROM categorias ORDER BY DESC;
        data = Categoria.objects.order_by('-id').all() # Variable que almacena la tabla a consultar
        datos_json = CategoriaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)


        