from rest_framework.generics import ListAPIView

from emprendedoras.models import Emprendedora
from emprendedoras.serializers import EmprendedoraSerializer


# Create your views here.
class EmprendedoraListView(ListAPIView):
    queryset = Emprendedora.objects.all()
    serializer_class = EmprendedoraSerializer
