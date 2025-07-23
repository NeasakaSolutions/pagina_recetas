# Importaciones
from django.db import models
from django.contrib.auth.models import User


class UsersMetadata(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    # Crear un token para verificaciones de la cuenta
    token = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        # Muestra el primer nombre y el apellido
        return f"{self.first_user} {self.last_name}"
    
    class Meta:
        db_table = 'users_metadata'
        verbose_name = "User metadata"
        verbose_name_plural = "User metadata"