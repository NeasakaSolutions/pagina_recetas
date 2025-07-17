# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
# Modelos de la bases de datos:
from categorias.models import Categoria
from recetas.models import Receta

# Busqueda en conjunto
class Clase1(APIView):

    # Funcion para agregar datos
    def post(self, request):
        # Validaciones para que los campos no esten vacios:
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio."})
        if request.data.get("correo") == None or not request.data["correo"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio."})
        if request.data.get("telefono") == None or not request.data["telefono"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo telefono es obligatorio."})
        if request.data.get("mensaje") == None or not request.data["mensaje"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo mensaje es obligatorio."})
        

