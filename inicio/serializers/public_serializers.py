from rest_framework import serializers

from inicio.models import CarruselInicioImagen


class CarruselInicioImagenPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarruselInicioImagen
        exclude = ['id']