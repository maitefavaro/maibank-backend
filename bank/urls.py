from django.urls import path, include
from rest_framework import routers
from .views import (
    UsuarioViewSet, ContaViewSet, CartaoViewSet
)
router = routers.DefaultRouter()

router.register("usuario",UsuarioViewSet)
router.register("conta", ContaViewSet)
router.register("cartao", CartaoViewSet)

urlpatterns = [
    path("",include(router.urls)),

]   