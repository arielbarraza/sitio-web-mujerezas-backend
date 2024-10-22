from rest_framework import serializers

from inicio.models import CarruselInicioImagen


class CarruselInicioImagenAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarruselInicioImagen
        fields = '__all__'
        read_only_fields = ('posicion',)

    def create(self, validated_data):
        queryset = CarruselInicioImagen.objects.all().order_by('posicion')

        if len(queryset) == 0:
            posicion = 1
        else:
            posicion = queryset.last().posicion + 1

        validated_data['posicion'] = posicion
        return super().create(validated_data)


class CarruselInicioImagenOrdenarEliminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarruselInicioImagen
        fields = ['id', 'posicion']
