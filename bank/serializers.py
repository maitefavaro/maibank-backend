from rest_framework.serializers import ModelSerializer, Serializer
from .models import(
    Conta, Usuario, Cartao
)

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class ContaSerializer(ModelSerializer):
    class Meta:
        model = Conta
        fields = "__all__"
        
class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = "__all__"