from django.urls import path

from capsulas.views.public_views import PublicCapsulasListView, PublicCapsulasDestacadasView

urlpatterns = [
    path(r'todas/', PublicCapsulasListView.as_view(), name=r'capsulas_list'),
    path(r'destacadas/', PublicCapsulasDestacadasView.as_view(), name=r'capsulas_destacadas'),
]
