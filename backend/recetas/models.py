# Importaciones
from django.db import models
from autoslug import AutoSlugField
from categorias.models import Categoria

# Creacion del modelo en la BD
class Receta(models.Model):
    # Llave foranea
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, default = 1)

    # Configuracion de los demas registros
    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre', max_length = 100)
    tiempo = models.CharField(max_length = 100, null = True)
    foto = models.CharField(max_length = 100, null = True)
    descripcion = models.TextField()
    # Con auto_now genera el registro de fecha de forma automatica
    fecha = models.DateTimeField(auto_now = True)


    # Buenas practicas de programacion: (OPCIONAL)
    def __str__(self):
        return self.nombre # Muestra el contenido del campo que se establezca
    
    # Nombre que recibira la tabla en el administrador de django
    class Meta:
        db_table = 'recetas'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'