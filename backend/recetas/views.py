# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

# Clases
class Clase1(APIView):

    def get (self, request):
        pass
