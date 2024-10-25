from django.urls import path

from inicio.views.admin_views import AdminCarruselInicioImagenCreateView, AdminCarruselInicioImagenListView, \
    AdminCarruselInicioImagenRetrieveView, AdminCarruselInicioImagenUpdateView, AdminCarruselInicioOrdenarView

urlpatterns = [
    path(r'todas/', AdminCarruselInicioImagenListView.as_view(), name=r'inicio_carrusel_admin_todas'),
    path(r'detalle/<pk>/', AdminCarruselInicioImagenRetrieveView.as_view(), name=r'inicio_carrusel_admin_detalle'),
    path(r'anadir/', AdminCarruselInicioImagenCreateView.as_view(), name=r'inicio_carrusel_admin_anadir'),
    path(r'editar/<pk>/', AdminCarruselInicioImagenUpdateView.as_view(), name=r'inicio_carrusel_admin_editar'),
    path(r'ordenar/', AdminCarruselInicioOrdenarView.as_view(), name=r'inicio_carrusel_admin_eliminar'),
]
