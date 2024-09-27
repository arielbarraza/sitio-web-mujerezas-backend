from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from noticias.models import Noticia
from noticias.serializers.public_serializers import PublicNoticiasListSerializer, PublicNoticiaDetalleSerializer


class PublicNoticiasListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Noticia.objects.all().order_by('-fecha_creacion')
    serializer_class = PublicNoticiasListSerializer


class PublicNoticiasDestacadasView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Noticia.objects.filter(destacada=True).order_by('-fecha_creacion')
    serializer_class = PublicNoticiasListSerializer


class PublicNoticiaDetalleView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Noticia.objects.all()
    serializer_class = PublicNoticiaDetalleSerializer
