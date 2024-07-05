from rest_framework import serializers

from emprendedoras.models import Emprendedora, Producto


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['imagen']


class EmprendedoraSerializer(serializers.ModelSerializer):
    productos = ImagenSerializer(many=True)

    class Meta:
        model = Emprendedora
        exclude = ['id']
