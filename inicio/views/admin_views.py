from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class AdminCarruselInicioOrdenarView(APIView):
    queryset = CarruselInicioImagen.objects.all()
    serializer_class = CarruselInicioImagenAdminSerializer

    def get_object(self, obj_id):
        try:
            return CarruselInicioImagen.objects.get(id=obj_id)
        except (CarruselInicioImagen.DoesNotExist, ValidationError):
            raise status.HTTP_400_BAD_REQUEST

    def put(self, request, *args, **kwargs):

        ids = list(map(lambda x: x['id'], request.data))

        #delete
        CarruselInicioImagen.objects.all().exclude(id__in=ids).delete()

        #update position
        objetos = CarruselInicioImagen.objects.filter(id__in=ids).order_by('posicion')
        for obj in objetos:
            for data in request.data:
                if data['id'] == obj.id:
                    print(obj.posicion)
                    print(data['posicion'])
                    obj.posicion = data['posicion']
        CarruselInicioImagen.objects.bulk_update(objetos, ["posicion"])
        data = CarruselInicioImagenAdminSerializer(instance=objetos, many=True).data

        return Response(data, status=status.HTTP_200_OK)
