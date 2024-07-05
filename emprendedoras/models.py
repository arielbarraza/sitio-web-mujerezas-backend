from django.db import models


class Producto(models.Model):
    imagen = models.ImageField(upload_to='imagenes/productos')


class Emprendedora(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    informacion = models.TextField()
    correo = models.EmailField()
    foto = models.ImageField(upload_to='imagenes/emprendedoras')
    telefono = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto)
