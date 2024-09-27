from django.urls import path

from noticias.views import NoticiasListView

urlpatterns = [
    path(r'todas/', NoticiasListView.as_view(), name=r'noticias_list'),
]
