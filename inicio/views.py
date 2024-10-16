from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from inicio.models import CarruselInicioImagen
from inicio.serializers.admin_serializers import CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenListView(ListAPIView):
    serializer_class = CarruselInicioImagenAdminSerializer
    queryset = CarruselInicioImagen.objects.all().order_by('posicion')


class AdminCarruselInicioImagenRetrieveView(RetrieveAPIView):
    queryset = CarruselInicioImagen.objects.all()
    serializer_class = CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenCreateView(CreateAPIView):
    serializer_class = CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenUpdateView(UpdateAPIView):
    queryset = CarruselInicioImagen.objects.all()
    serializer_class = CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenDestroyView(DestroyAPIView):
    queryset = CarruselInicioImagen.objects.all()
