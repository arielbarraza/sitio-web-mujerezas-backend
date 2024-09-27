from rest_framework import serializers

from noticias.models import Noticia


class NoticiasAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
