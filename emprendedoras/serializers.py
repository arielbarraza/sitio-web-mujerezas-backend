from rest_framework import serializers

from emprendedoras.models import Emprendedora


class EmprendedoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendedora
        fields = '__all__'
