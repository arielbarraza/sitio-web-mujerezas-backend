from django.urls import path

from inicio.views import AdminCarruselInicioImagenCreateView, AdminCarruselInicioImagenListView

urlpatterns = [
    path(r'todas/', AdminCarruselInicioImagenListView.as_view(), name=r'inicio_carrusel_admin_todas'),
    #path(r'detalle/<pk>/', AdminNoticiasRetrieveView.as_view(), name=r'noticias_admin_detalle'),
    path(r'anadir/', AdminCarruselInicioImagenCreateView.as_view(), name=r'inicio_carrusel_admin_anadir'),
    #path(r'editar/<pk>/', AdminNoticiasUpdateView.as_view(), name=r'noticias_admin_editar'),
    #path(r'eliminar/<pk>/', AdminNoticiasDestroyView.as_view(), name=r'noticias_admin_eliminar'),
]
