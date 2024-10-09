from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from capsulas.models import Capsula
from capsulas.serializers.admin_serializers import CapsulasAdminSerializer


class AdminCapsulasListView(ListAPIView):
    queryset = Capsula.objects.all()
    serializer_class = CapsulasAdminSerializer


class AdminCapulaCreateView(CreateAPIView):
    serializer_class = CapsulasAdminSerializer


class AdminCapsulaDestroyView(DestroyAPIView):
    queryset = Capsula.objects.all()
