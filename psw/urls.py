"""psw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    #Painel do administrador
    path('admin/', admin.site.urls),

    #rotas de login
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token), #usar postman

    #rota de produtos
    path('products/', include('products.urls')),

    #rota de contas
    path('accounts/', include('accounts.urls')),
]
