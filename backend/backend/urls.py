# Importaciones
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Es la pagina principal de Django y no puede ser modificada
    path('admin/', admin.site.urls),
    # Ruta principal creada por nosotros
    path('', include('home.urls')),
    path('api/v1/', include('categorias.urls')),
    path('api/v1/', include('recetas.urls')),
    path('api/v1/', include('contacto.urls')),
]

# Url para configuracion de los archivos que se van a mostrar
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
