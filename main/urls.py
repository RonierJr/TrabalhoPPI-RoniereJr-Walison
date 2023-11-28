"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from shoes.views import IndexHomeView,TenisDetailView,TenisListView,TenisDeleteView,TenisCreateView,TenisUpdateView,MarcaListView,MarcaCreateView,MarcaDeleteView,MarcaUpdateView,AdmHomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',IndexHomeView.as_view(), name='index'),
    path('tenis/<int:pk>/',TenisDetailView.as_view(),name='detalhe_tenis'),
    path('tenis_listar',TenisListView.as_view(),name='tenis_listar'),
    path('tenis/',TenisCreateView.as_view(),name='tenis_criar'),
    path('tenis/editar/<int:pk>/',TenisUpdateView.as_view(),name='tenis_editar'),
    path('tenis/remover/<int:pk>/',TenisDeleteView.as_view(),name='tenis_remover'),
    path('marca_listar',MarcaListView.as_view(),name='marca_listar'),
    path('marca/',MarcaCreateView.as_view(),name='marca_criar'),
    path('marca/remover/<int:pk>/',MarcaDeleteView.as_view(),name='marca_remover'),
    path('marca/editar/<int:pk>/',MarcaUpdateView.as_view(),name='marca_editar'),
    path('administracao',AdmHomeView.as_view(),name='administracao'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
