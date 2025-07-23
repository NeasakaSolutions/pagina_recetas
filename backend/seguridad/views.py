# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
# Modelos de las bases de datos
from categorias.models import Categoria
from django.contrib.auth.models import User

# Clases
class Clase1(APIView):
    
    def post(self, request):
        # Validacion para el campo del nombre
        if request.data.get("nombre") == None or not request.data.get("nombre"):
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion para el campo del correo
        if request.data.get("correo") == None or not request.data.get("correo"):
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion para la contraseña
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "mensaje": "El campo password es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion para que no se repita el correo:
        if User.objects.filter(email = request.data["correo"]).exists():
            return JsonResponse({"estado": "error", "mensaje": f"El correo {request.data["correo"]} ya existe."}, 
                                 status = HTTPStatus.BAD_REQUEST)
