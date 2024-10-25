from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from inicio.models import CarruselInicioImagen
from inicio.serializers.public_serializers import CarruselInicioImagenPublicSerializer


class PublicCarruselInicioImagenListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = CarruselInicioImagen.objects.all().order_by('posicion')
    serializer_class = CarruselInicioImagenPublicSerializer
