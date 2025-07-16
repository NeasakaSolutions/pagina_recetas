# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from categorias.serializers import CategoriaSerializer
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
# Tabla que se usara para realizar las consultas
from categorias.models import Categoria 
from recetas.models import Receta

# Clases de la aplicacion
class Clase1(APIView):

    # Funcion para mostrar datos
    def get(self, request):
        
        # SELECT * FROM categorias ORDER BY DESC;
        data = Categoria.objects.order_by('-id').all() # Variable que almacena la tabla a consultar
        datos_json = CategoriaSerializer(data, many = True)
        # Retorno
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)
    
    # Funcion para agregar datos
    def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        try:
            # Crear registro
            Categoria.objects.create(nombre = request.data['nombre'])
            # Retorno
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
            # Retorno
            return JsonResponse({"data": {"id": data.id ,"nombre": data.nombre, "slug": data.slug}},
                             status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        
    # Funcion para editar una categoria
    def put(self, request, id):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        
        try:
            # Busca el registro
            data = Categoria.objects.filter(pk = id).get()
            # Modificar en caso de que si encuentre el registro
            Categoria.objects.filter(pk = id).update(nombre = request.data.get("nombre"),
                                    slug = slugify(request.data.get("nombre")))
            # Retorno
            return JsonResponse({"estado": "ok", "mensaje": "Se modifico el registro correctamente"},
                                 status = HTTPStatus.OK)

        except Categoria.DoesNotExist:
            raise Http404
        
    # Metodo para eliminar registros
    def delete(self, request, id):
         
        try:
            # Busca el registro
            data = Categoria.objects.filter(pk = id).get()
        except Categoria.DoesNotExist:
            raise Http404
        
        if Receta.objects.filter(categoria_id = id).exists():
            return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Eliminar en caso de que si encuentre el registro
        Categoria.objects.filter(pk = id).delete()
        # Retorno
        return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro correctamente"},
                            status = HTTPStatus.OK)

        