from django.urls import path

from inicio.views.public_views import PublicCarruselInicioImagenListView

urlpatterns = [
    path(r'todas/', PublicCarruselInicioImagenListView.as_view(), name=r'inicio_carrusel_public_todas'),
]
