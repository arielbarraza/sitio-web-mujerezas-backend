from django.urls import path

from noticias.views.admin_views import AdminNoticiasListView, AdminNoticiasCreateView

urlpatterns = [
    path(r'todas/', AdminNoticiasListView.as_view(), name=r'noticias_admin_todas'),
    path(r'crear/', AdminNoticiasCreateView.as_view(), name=r'noticias_admin_crear')
]
