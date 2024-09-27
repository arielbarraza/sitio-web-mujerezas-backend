from django.urls import path

from noticias.views import NoticiasAdminListView, NoticiasCreateView

urlpatterns = [
    path(r'todas/', NoticiasAdminListView.as_view(), name=r'noticias_admin_todas'),
    path(r'crear/', NoticiasCreateView.as_view(), name=r'noticias_admin_crear')
]
