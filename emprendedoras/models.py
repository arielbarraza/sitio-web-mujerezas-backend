from django.db import models


class ImagenEmprendimiento(models.Model):
    imagen = models.ImageField(upload_to='imagens/')


class Emprendedora(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    informacion = models.TextField()
    correo = models.EmailField()
    foto = models.ImageField(upload_to='fotos/')
    telefono = models.CharField(max_length=50)
    productos = models.ManyToManyField(ImagenEmprendimiento)
