# Importaciones
from django.shortcuts import render
from django.http import HttpResponse

# Funcion de prueba
def home_inicio(request):
    return HttpResponse('<h1>Hola mundo desde Django</h1>')

