# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
import uuid
import os
from dotenv import load_dotenv
from utilidades import utilidades
# Modelos de las bases de datos
from seguridad.models import UsersMetadata
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

        # Variable token
        token = uuid.uuid4()
        url = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion{token}"
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
