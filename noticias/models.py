from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    bajada = models.TextField(null=True, blank=True)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="imagenes/noticias")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

