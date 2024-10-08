from django.urls import path

from noticias.views.admin_views import AdminNoticiasListView, AdminNoticiasCreateView, AdminNoticiasDestroyView, \
    AdminNoticiasRetrieveView, AdminNoticiasUpdateView, AdminNoticiasDestacarView

urlpatterns = [
    path(r'todas/', AdminNoticiasListView.as_view(), name=r'noticias_admin_todas'),
    path(r'detalle/<pk>/', AdminNoticiasRetrieveView.as_view(), name=r'noticias_admin_detalle'),
    path(r'crear/', AdminNoticiasCreateView.as_view(), name=r'noticias_admin_crear'),
    path(r'editar/<pk>/', AdminNoticiasUpdateView.as_view(), name=r'noticias_admin_editar'),
    path(r'eliminar/<pk>/', AdminNoticiasDestroyView.as_view(), name=r'noticias_admin_eliminar'),
    path(r'destacar/<pk>/', AdminNoticiasDestacarView.as_view(), name=r'noticias_admin_destacar'),
]
