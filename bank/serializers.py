from rest_framework.serializers import ModelSerializer, Serializer
from .models import *


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


class FaturaSerializer(ModelSerializer):
    class Meta:
        model = Fatura
        fields = "__all__"


class TransacaoSerializer(ModelSerializer):
    class Meta:
        model = Transacao
        fields = "__all__"


class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"


class PagEmprestimoSerialzer(ModelSerializer):
    class Meta:
        model = Pag_emprestimo
        fields = "__all__"


class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favoritos
        fields = "__all__"


class ExtratoSerializer(ModelSerializer):
    class Meta:
        model = Extrato
        fields = "__all__"
