# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from http import HTTPStatus
import uuid
import os
from dotenv import load_dotenv
from utilidades import utilidades
from django.contrib.auth import authenticate
from jose import jwt
from django.conf import settings
from datetime import datetime
from datetime import timedelta
import time
# Modelos de las bases de datos
from seguridad.models import UsersMetadata
from django.contrib.auth.models import User

# Clase para registrar:
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

        # Variable token
        token = uuid.uuid4()
        url = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}"
        try:
            # Creacion del usuario
            u = User.objects.create_user(username = request.data["correo"], password = request.data["password"], 
                                        email = request.data["correo"], first_name = request.data["nombre"], 
                                        last_name = "", is_active = 0)
            
            UsersMetadata.objects.create(token = token, user_id = u.id)

            # Correo de verificacion:
            html = f"""
                    <h3>Verificacion de cuenta</h3>
                    Hola {request.data["nombre"]} te haz registrado exitosamente. Para activar tu cuenta haz click en 
                    el siguiente enlace: <br/>
                    <a href="{url}">{url}</a>
                    <br/>
                    O copia y pega la siguiente url en tu navegador favorito:
                    <br/>
                    {url}
                      """
            utilidades.sendMail(html, "Verificacion", request.data["correo"])

        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado."}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente."}, 
                                status = HTTPStatus.CREATED)

# Clase para validar:
class Clase2(APIView):

    def get(self, request, token):
        
        # Validacion del token:
        if token == None or not token:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, 
                                status = 404)
        try:
            # Busca un registro con el token dado donde el is_active sea igual a 0 y lo guarda en data
            data = UsersMetadata.objects.filter(token = token).filter(user__is_active = 0).get()
            # Luego borra ese token de la base de datos, dejándolo vacío
            UsersMetadata.objects.filter(token = token).update(token = "")
            # Cambia el activo a 1, significa que ya se valido el usuario
            User.objects.filter(id = data.user_id).update(is_active = 1)
            # Redireccionamos al usuario al fronted del login
            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTED"))
        except UsersMetadata.DoesNotExist:
            raise Http404
        
# Clase para login:
class Clase3(APIView):

    def post(self, request):
        # Validaciones:
        if request.data.get("correo") == None or not request.data.get("correo"):
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "mensaje": "El campo password es obligatorio"}, 
                                status = HTTPStatus.BAD_REQUEST)
        
        try:
            # SELECT * FROM auth_user WHERE correo = correo
            user = User.objects.filter(email = request.data["correo"]).get()
        except User.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "El correo ingresado no es valido."}, 
                                status = HTTPStatus.NOT_FOUND)
        
        # Validacion de la password
        auth = authenticate(request, username = request.data.get("correo"), password = request.data.get("password"))

        if auth is not None:
            fecha = datetime.now()
            # Vigencia del token
            despues = fecha + timedelta(days = 1)
            # Se usa cuando se suben archivos al servidor
            fecha_numero = int(datetime.timestamp(despues))
            payload = {"id": user.id, "ISS": os.getenv("BASE_URL"), "iat": int(time.time()), 
                       "exp": int(fecha_numero)}
            
            # Crear el token:
            try:
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm = 'HS512')
                return JsonResponse({"id": user.id, "nombre": user.first_name, "token": token})
            except Exception as e:
                return JsonResponse({"estado": "error", "mensaje": "Ocurrio un error inesperado."}, 
                                     status = HTTPStatus.BAD_REQUEST)
        else:
            return JsonResponse({"estado": "error", "mensaje": "La password ingresada no es valida."}, 
                                status = HTTPStatus.BAD_REQUEST)


