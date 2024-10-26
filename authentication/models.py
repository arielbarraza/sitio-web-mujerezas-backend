from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from authentication.managers import CustomUserManager


# Create your models here.
class Usuario(AbstractBaseUser):
    ROLES = (
        ('ADMINISTRADOR', 'Administrador'),
        ('PUBLICADOR', 'Publicador'),
    )

    rut = models.CharField('Rut', max_length=255, unique=True)
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rol = models.CharField(max_length=20, choices=ROLES)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = ['correo_electronico']
    objects = CustomUserManager()

