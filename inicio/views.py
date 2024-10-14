from rest_framework.generics import CreateAPIView, ListAPIView

from inicio.models import CarruselInicioImagen
from inicio.serializers.admin_serializers import CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenListView(ListAPIView):
    serializer_class = CarruselInicioImagenAdminSerializer
    queryset = CarruselInicioImagen.objects.all().order_by('posicion')

class AdminCarruselInicioImagenCreateView(CreateAPIView):
    serializer_class = CarruselInicioImagenAdminSerializer
