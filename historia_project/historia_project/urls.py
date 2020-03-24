"""historia_project URL Configuration

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
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import DefaultRouter

from genero.views import GeneroViewset
from categoria.views import TipoCategoriaViewset, CategoriaViewset
from autor.views import AutorViewset

router = DefaultRouter()
router.register(r'generos',GeneroViewset, "genero")
router.register(r'tipos_categoria', TipoCategoriaViewset, "tipos_categoria")
router.register(r'categorias',CategoriaViewset,"categorias")
router.register(r'autores', AutorViewset, "autores")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('api/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh_token/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
