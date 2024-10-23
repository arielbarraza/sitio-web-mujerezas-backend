from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from capsulas.models import Capsula
from capsulas.serializers.public_serializers import PublicCapsulasListSerializer


class PublicCapsulasListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Capsula.objects.all().order_by('-fecha_creacion')
    serializer_class = PublicCapsulasListSerializer


class PublicCapsulasDestacadasView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Capsula.objects.filter(destacada=True).order_by('-fecha_creacion')
    serializer_class = PublicCapsulasListSerializer
