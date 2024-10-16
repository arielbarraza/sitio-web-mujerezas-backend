from django.urls import path

from inicio.views import AdminCarruselInicioImagenCreateView, AdminCarruselInicioImagenListView, \
    AdminCarruselInicioImagenRetrieveView, AdminCarruselInicioImagenUpdateView, AdminCarruselInicioImagenDestroyView

urlpatterns = [
    path(r'todas/', AdminCarruselInicioImagenListView.as_view(), name=r'inicio_carrusel_admin_todas'),
    path(r'detalle/<pk>/', AdminCarruselInicioImagenRetrieveView.as_view(), name=r'inicio_carrusel_admin_detalle'),
    path(r'anadir/', AdminCarruselInicioImagenCreateView.as_view(), name=r'inicio_carrusel_admin_anadir'),
    path(r'editar/<pk>/', AdminCarruselInicioImagenUpdateView.as_view(), name=r'inicio_carrusel_admin_editar'),
    path(r'eliminar/<pk>/', AdminCarruselInicioImagenDestroyView.as_view(), name=r'inicio_carrusel_admin_eliminar'),
]
