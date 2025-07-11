from django.db import models
from autoslug import AutoSlugField

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre')

    # Buenas practicas de programacion: (OPCIONAL)
    def __str__(self):
        return self.nombre # Muestra el contenido del campo que se establezca
    
    # Nombre que recibira la tabla en el administrador de django
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

