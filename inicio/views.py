from rest_framework.generics import CreateAPIView

from inicio.serializers.admin_serializers import CarruselInicioImagenAdminSerializer


class AdminCarruselInicioImagenCreateView(CreateAPIView):
    serializer_class = CarruselInicioImagenAdminSerializer
