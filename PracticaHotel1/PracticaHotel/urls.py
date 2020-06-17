"""PracticaHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
from HotelSayula.views import RegistrarUsuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include ('HotelSayula.urls',namespace=None)),
    path('accounts/login/', LoginView.as_view(template_name='HotelSayula/login.html'), name="login"),
    path('logout',logout_then_login,name='logout'),
    path('crear_usuario',RegistrarUsuario.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
