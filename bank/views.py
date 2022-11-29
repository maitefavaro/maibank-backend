from .models import (
    Cartao, Conta, Usuario
)
from rest_framework.viewsets import ModelViewSet 
from rest_framework.views import APIView
from .serializers import (
    CartaoSerializer,ContaSerializer,UsuarioSerializer
)

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ContaViewSet(ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer