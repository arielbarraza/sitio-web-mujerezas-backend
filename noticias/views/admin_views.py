from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from noticias.models import Noticia
from noticias.serializers.admin_serializers import NoticiasAdminListSerializer, NoticiasAdminDestacadaSerializer


# Create your views here.
class AdminNoticiasListView(ListAPIView):
    serializer_class = NoticiasAdminListSerializer
    queryset = Noticia.objects.all().order_by('-fecha_creacion')


class AdminNoticiasRetrieveView(RetrieveAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasAdminListSerializer


class AdminNoticiasCreateView(CreateAPIView):
    serializer_class = NoticiasAdminListSerializer


class AdminNoticiasUpdateView(UpdateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasAdminListSerializer


class AdminNoticiasDestroyView(DestroyAPIView):
    queryset = Noticia.objects.all()


class AdminNoticiasDestacarView(UpdateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasAdminDestacadaSerializer
