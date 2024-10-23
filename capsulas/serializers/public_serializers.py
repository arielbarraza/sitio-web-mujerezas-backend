from rest_framework import serializers

from capsulas.models import Capsula


class PublicCapsulasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsula
        fields = ['id', 'titulo', 'descripcion', 'archivo']