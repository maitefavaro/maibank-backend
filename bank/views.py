import decimal
from .models import *
from rest_framework.viewsets import ModelViewSet 
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LogarViewSet(ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class = LogarSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        objUsuario = Usuario.objects.filter(cpf=self.request.data['cpf'], senha=self.request.data['senha'])
        if objUsuario:
            print("logado")
            return Response(status=status.HTTP_200_OK)
        else:
            print("erro")
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ContaViewSet(ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class FaturaViewSet(ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

class TransacaoViewSet(ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def create(self, request, *args, **kwargs):
        beneficiario = Conta.objects.get(pk=self.request.data
        ["beneficiario"])
        beneficiado = Conta.objects.get(pk=self.request.data
        ["beneficiado"])
        valor = decimal.Decimal(self.request.data
        ["valor_transacao"])

        if beneficiario.saldo >= valor:
            env = {'usuario':beneficiario.pk,'conta':beneficiario.conta,'agencia':beneficiario.agencia,'saldo':beneficiario.saldo-valor}
            serializer = ContaSerializer(beneficiario, data=env)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

            rec = {'usuario':beneficiado.pk,'agencia':beneficiado.agencia,'conta':beneficiado.conta,'saldo':beneficiado.saldo+valor}

            serializer_dois = ContaSerializer(beneficiado,data=rec)
            if serializer_dois.is_valid():
                serializer_dois.save()

            else:
                print(serializer.errors)

        return super().create(request,*args,**kwargs)

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class PagEmprestimoViewSet(ModelViewSet):
    queryset = Pag_Emprestimo.objects.all()
    serializer_class = PagEmprestimoSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer

class ExtratoViewSet(ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer
    