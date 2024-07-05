from django.urls import path

from emprendedoras.views import EmprendedoraListView

urlpatterns = [
    path(r'', EmprendedoraListView.as_view(), name='emprendedoras'),
]