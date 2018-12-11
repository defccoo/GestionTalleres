"""talleres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('inicio/', views.homepage, name='homepage'),
    path('principal/', views.doLogin, name='login'),
    path('access/', views.acceso, name='acceso'),
    path('local/', views.sitio, name='sitio'),
    path('logout/', views.logout_view, name='logout'),
    path('inscribir/', views.inscribirse, name='inscribir'),
    path('error/', views.error_view, name='error_log'),
    path('contact/', views.contacto, name='contact'),
    path('listar/', views.listataller, name='listataller'),
    path('taller/listar', views.listataller, name='listataller'),
    path('taller/alta', views.taller_new, name='altataller'),
    path('taller/crear', views.creartaller, name='creartaller'),

    #Mostrar lista taller...leer todos los talleres y mostrarlos con los enlaces a /taller/mostrar/taller_id
    path('taller/mostrar/<int:taller_id>', views.muestraTallerConID, name='muestraTallerConID'),
   
    url('^taller/update/(?P<pk>[\w-]+)$', views.TallerUpdateView.as_view(), name='taller_update'),
    url('^taller/delete/(?P<pk>[\w-]+)$', views.TallerDelete.as_view(), name='taller_delete'),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


