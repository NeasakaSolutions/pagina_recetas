# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from recetas.serializers import RecetaSerializer
from recetas.models import Receta
from categorias.models import Categoria
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Clase para busquedas grupales
class Clase1(APIView):

    # Funcion para mostrar todos los registros
    def get (self, request):

        # Listar todos los id ordenados de mayor a menor
        data = Receta.objects.order_by('-id').all()
        datos_json = RecetaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data})
    
    # Funcion para agregar datos
    def post(self, request):
        # Validacion del nombre
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion del tiempo
        if request.data.get("tiempo") == None or not request.data["tiempo"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo tiempo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion de la descripcion:
        if request.data.get("descripcion") == None or not request.data["descripcion"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo descripcion es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion de la categoria_id:
        if request.data.get("categoria_id") == None or not request.data["categoria_id"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo categoria es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        # Validacion para no repetir registros:
        # Validacion para el campo categoria (valida que exista)
        try:
            # Consulta
            categoria = Categoria.objects.filter(pk = request.data["categoria_id"]).get()
        except Categoria.DoesNotExist:
            # Retorno
            return JsonResponse({"estado": "error", "mensaje": "La categoria no existe en la base de datos."}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        # SELECT * FROM recetas WHERE nombre = request.data.get("nombre")
        if Receta.objects.filter(nombre = request.data.get("nombre")).exists():
            # Retorno:
            return JsonResponse({"estado": "error", "mensaje": f"El nombre {request.data["nombre"]} no esta disponible"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        # Configuraciones para la imagen
        fs = FileSystemStorage()
        try:
            # Nombre de la foto
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "Debe de adjuntar una foto en el campo foto"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        # Validacion MIME:
        if request.FILES["foto"].content_type == "image/jpeg" or request.FILES["foto"].content_type == "image/png":

            # Almacenar la imagen
            try:
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url(request.FILES['foto'])
            except Exception as e:
                return JsonResponse({"estado": "error", "mensaje": "Se produjo un error al intentar subir el archivo"}, 
                                    status = HTTPStatus.BAD_REQUEST)

            # Manejo de errores
            try:
                Receta.objects.create(nombre = request.data["nombre"], tiempo = request.data.get("tiempo"),
                                    descripcion = request.data["descripcion"], categoria_id = request.data.get("categoria_id"), 
                                    fecha = datetime.now(), foto = foto)
                # Retorno
                return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente"}, 
                                    status = HTTPStatus.CREATED)
            except Exception as e:
                raise Http404
            
        return JsonResponse({"estado": "error", "mensaje": "La foto solo puede ser png y jpg"}, 
                            status = HTTPStatus.BAD_REQUEST)
    
# Clase para busqueda individual:
class Clase2(APIView):

    # Funcion para buscar registros de forma individual
    def get(self, request, id):
        try:
            data = Receta.objects.filter(id = id).get()
            # Retorno
            return JsonResponse({"data": {"id" : data.id, "nombre": data.nombre, "slug": data.slug, 
                                "tiempo": data.tiempo, "descripcion": data.descripcion, 
                                "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id, 
                                "categoria" : data.categoria.nombre, 
                                "imagen": f"{os.getenv("BASE_URL")}uploads/recetas/{data.foto}"}}, 
                                status = HTTPStatus.OK)
        # Retorno
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, 
                                status = HTTPStatus.NOT_FOUND)

    # Funcion para editar un registro:
    def put(self, request, id):
        
        # Buscar que el dato exista
        try:
            data = Receta.objects.filter(id = id).get()
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, 
                                status = HTTPStatus.NOT_FOUND)
        
        # Validacion del nombre
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion del tiempo
        if request.data.get("tiempo") == None or not request.data["tiempo"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo tiempo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion de la descripcion:
        if request.data.get("descripcion") == None or not request.data["descripcion"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo descripcion es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        # Validacion de la categoria_id:
        if request.data.get("categoria_id") == None or not request.data["categoria_id"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo categoria es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        # Validacion para el campo categoria (valida que exista)
        try:
            # Consulta
            categoria = Categoria.objects.filter(pk = request.data["categoria_id"]).get()
        except Categoria.DoesNotExist:
            # Retorno
            return JsonResponse({"estado": "error", "mensaje": "La categoria no existe en la base de datos."}, 
                                status = HTTPStatus.BAD_REQUEST)

        # Modificar el registro
        try:
            Receta.objects.filter(pk = id).update(nombre = request.data["nombre"], slug = slugify(request.data["nombre"]),  
                                                  tiempo = request.data["tiempo"], descripcion = request.data["descripcion"], 
                                                  categoria_id = request.data["categoria_id"])
            # Retorno
            return JsonResponse({"estado": "ok", "mensaje": "Se modifico el registro exitosamente"}, 
                                status = HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado"}, 
                                status = HTTPStatus.NOT_FOUND)
        
    def delete(self, request, id):
        try:
            # Verificar que el registro exista en la BD
            data = Receta.objects.filter(id = id).get()
        except Receta.DoesNotExist:
            # Retorno
            return JsonResponse({"estado": "error", "mensaje": "La receta que se intenta eliminar no existe"}, 
                                status = HTTPStatus.NOT_FOUND)
        
        # Borrar la foto de la carpeta
        os.remove(f"./uploads/recetas/{data.foto}")

        # Borrar el registro de la BD
        Receta.objects.filter(id = id).delete()
        # Retorno
        return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro"}, 
                            status = HTTPStatus.OK)

