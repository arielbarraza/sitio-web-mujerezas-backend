from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from noticias.models import Noticia
from noticias.serializers import NoticiasAdminListSerializer, NoticiasListSerializer


# Create your views here.
class NoticiasAdminListView(ListAPIView):
    serializer_class = NoticiasAdminListSerializer
    queryset = Noticia.objects.all().order_by('-fecha_creacion')


class NoticiasCreateView(CreateAPIView):
    serializer_class = NoticiasAdminListSerializer


class NoticiasListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Noticia.objects.all().order_by('-fecha_creacion')
    serializer_class = NoticiasListSerializer
