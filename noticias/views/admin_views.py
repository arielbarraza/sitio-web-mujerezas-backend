from rest_framework.generics import ListAPIView, CreateAPIView

from noticias.models import Noticia
from noticias.serializers.admin_serializers import NoticiasAdminListSerializer


# Create your views here.
class AdminNoticiasListView(ListAPIView):
    serializer_class = NoticiasAdminListSerializer
    queryset = Noticia.objects.all().order_by('-fecha_creacion')


class AdminNoticiasCreateView(CreateAPIView):
    serializer_class = NoticiasAdminListSerializer


