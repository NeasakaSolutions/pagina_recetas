# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from categorias.serializers import CategoriaSerializer
from http import HTTPStatus
from django.http import Http404
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
    
    # Funcion para agregar datos
    def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        try:
            # Crear registro
            Categoria.objects.create(nombre = request.data['nombre'])
            return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente"},
                                 status = HTTPStatus.CREATED)
        # Excepcion general
        except Exception as e:
            raise Http404

# Busqueda individual    
class Clase2(APIView):

    # Funcion para mostrar un dato especifico
    def get(self, request, id):
        try:
            # SELECT * FROM categorias WHERE id = 4;
            data = Categoria.objects.filter(id = id).get() # pk = id (primary key)
            return JsonResponse({"data": {"id": data.id ,"nombre": data.nombre, "slug": data.slug}},
                             status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404

        