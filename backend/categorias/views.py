from rest_framework.views import APIView
from django.http.response import JsonResponse

# Clases de la aplicacion
class Clase1(APIView):

    # Funcion para mostrar datos
    def get(self, request):
        pass