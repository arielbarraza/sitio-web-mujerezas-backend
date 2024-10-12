from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from capsulas.models import Capsula
from capsulas.serializers.admin_serializers import CapsulasAdminSerializer, CapsulasAdminDestacadaSerializer


class AdminCapsulasListView(ListAPIView):
    queryset = Capsula.objects.all()
    serializer_class = CapsulasAdminSerializer


class AdminCapsulaRetrieveView(RetrieveAPIView):
    queryset = Capsula.objects.all()
    serializer_class = CapsulasAdminSerializer


class AdminCapulaCreateView(CreateAPIView):
    serializer_class = CapsulasAdminSerializer


class AdminCapsulaUpdateView(UpdateAPIView):
    queryset = Capsula.objects.all()
    serializer_class = CapsulasAdminSerializer


class AdminCapsulaDestroyView(DestroyAPIView):
    queryset = Capsula.objects.all()

class AdminCapsulaDestacarView(UpdateAPIView):
    queryset = Capsula.objects.all()
    serializer_class = CapsulasAdminDestacadaSerializer