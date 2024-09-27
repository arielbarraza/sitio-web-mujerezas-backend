from rest_framework import serializers

from noticias.models import Noticia


class NoticiasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'


class NoticiasAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'imagen', 'bajada']
