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
from django.urls import path
from shoes.views import index,detalhe_tenis,tenis_listar,tenis_remover,tenis_criar,tenis_editar,marca_listar,marca_criar,marca_remover,marca_editar,administracao
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('tenis/<int:id_tenis>',detalhe_tenis,name='detalhe_tenis'),
    path('tenis_listar',tenis_listar,name='tenis_listar'),
    path('tenis/',tenis_criar,name='tenis_criar'),
    path('tenis/editar/<int:id>/',tenis_editar,name='tenis_editar'),
    path('tenis/remover/<int:id>/',tenis_remover,name='tenis_remover'),
    path('marca_listar',marca_listar,name='marca_listar'),
    path('marca/',marca_criar,name='marca_criar'),
    path('marca/remover/<int:id>/',marca_remover,name='marca_remover'),
    path('marca/editar/<int:id>/',marca_editar,name='marca_editar'),
    path('administracao',administracao,name='administracao'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
