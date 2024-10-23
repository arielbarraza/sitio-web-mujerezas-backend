from django.urls import path

from noticias.views.public_views import PublicNoticiasListView, PublicNoticiasDestacadasView, PublicNoticiaDetalleView

urlpatterns = [
    path(r'todas/', PublicNoticiasListView.as_view(), name=r'noticias_list'),
    path(r'destacadas/', PublicNoticiasDestacadasView.as_view(), name=r'noticias_destacadas'),
    path(r'detalle/<pk>/', PublicNoticiaDetalleView.as_view(), name=r'noticia_detalle'),
]
