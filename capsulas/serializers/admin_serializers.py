from rest_framework import serializers

from capsulas.models import Capsula


class CapsulasAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsula
        fields = '__all__'

class CapsulasAdminDestacadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsula
        fields = ['destacada']
