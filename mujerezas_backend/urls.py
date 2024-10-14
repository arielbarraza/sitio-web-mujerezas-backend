"""mujerezas_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('noticias/', include('noticias.urls.public_urls')),
    path('admin/noticias/', include('noticias.urls.admin_urls')),
    path('admin/capsulas/', include('capsulas.urls.admin_urls')),
    path('admin/inicio/carrusel/', include('inicio.urls.admin_urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
