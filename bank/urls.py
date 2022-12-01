from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register("usuario",UsuarioViewSet)
router.register("logar", LogarViewSet)
router.register("conta", ContaViewSet)
router.register("cartao", CartaoViewSet)
router.register("fatura", FaturaViewSet)
router.register("transacao", TransacaoViewSet)
router.register("emprestimo", EmprestimoViewSet)
router.register("pag_emprestimo", PagEmprestimoViewSet)
router.register("favorito", FavoritoViewSet)
router.register("extrato", ExtratoViewSet)

urlpatterns = router.urls