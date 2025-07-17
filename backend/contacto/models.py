# Importaciones
from django.db import models


# Create your models here.
class Contacto(models.Model):
    # Configuracion del campo nombre
    nombre = models.CharField(max_length = 100, blank = True, null = True)
    # Configuracion del campo correo
    correo = models.CharField(max_length = 100, blank = True, null = True)
    # Configuracion del campo telefono
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    # Configuracion del campo mensaje
    mensaje = models.TextField()
    # Configuracion del campo fecha
    fecha = models.DateTimeField()

    # El primer campo que queremos mostrar
    def __str__(self):
        return self.nombre
    
    # Informacion del administrador de Django
    class Meta:
        db_table = 'contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = "Contactos"
    

