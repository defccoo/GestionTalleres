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
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('principal/', views.homepage, name='homepage'),
    path('login/', views.acceso, name='acceso'),
    #path('taller/mostrar', views.muestraTaller, name='muestraTaller'),
    path('listar/', views.listataller, name='listataller'),
    path('taller/listar', views.listataller, name='listataller'),
    path('taller/alta', views.taller_new, name='altataller'),
    path('taller/crear', views.creartaller, name='creartaller'),

    #Mostrar lista taller...leer todos los talleres y mostrarlos con los enlaces a /taller/mostrar/taller_id
    path('taller/mostrar/<int:taller_id>', views.muestraTallerConID, name='muestraTallerConID'),
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    
]

