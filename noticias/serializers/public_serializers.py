from rest_framework import serializers

from noticias.models import Noticia


class PublicNoticiasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'bajada', 'imagen']