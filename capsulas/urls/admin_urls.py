from django.urls import path

from capsulas.views.admin_views import AdminCapulaCreateView, AdminCapsulasListView, AdminCapsulaDestroyView

urlpatterns = [
    path(r'todas/', AdminCapsulasListView.as_view(), name=r'capsulas_admin_todas'),
    #path(r'detalle/<pk>/', AdminNoticiasRetrieveView.as_view(), name=r'noticias_admin_detalle'),
    path(r'crear/', AdminCapulaCreateView.as_view(), name=r'capsulas_admin_crear'),
    #path(r'editar/<pk>/', AdminNoticiasUpdateView.as_view(), name=r'noticias_admin_editar'),
    path(r'eliminar/<pk>/', AdminCapsulaDestroyView.as_view(), name=r'capsulas_admin_eliminar'),
    #path(r'destacar/<pk>/', AdminNoticiasDestacarView.as_view(), name=r'noticias_admin_destacar'),
]
