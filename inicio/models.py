from django.db import models


class CarruselInicioImagen(models.Model):
    posicion = models.PositiveSmallIntegerField(unique=True)
    imagen = models.ImageField(upload_to='archivos/imagenes')
    url_redirect = models.URLField(null=True)
