from django.db import models


class Capsula(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    destacada = models.BooleanField(default=False)
