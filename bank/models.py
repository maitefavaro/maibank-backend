from django.db.models import *

class Usuario(Model):
    SEXO_MASCULINO = 'm'
    SEXO_FEMININO = 'f'

    SEXO_TIPOS = [
        (SEXO_MASCULINO, 'masculino'),
        (SEXO_FEMININO, 'feminino'),
    ]

    nome = CharField(max_length=125)
    email = EmailField()
    cpf = CharField(max_length=14)
    data_nascimento =DateField()
    sexo =CharField(max_length=1, choices=SEXO_TIPOS)
    senha =CharField(max_length=100)

    def __str__(self) -> str:
        return self.id



class Conta(Model):

    usuario =ForeignKey(Usuario, on_delete=DO_NOTHING)
    agencia =CharField(max_length=5)
    conta  =CharField(max_length=8)
    saldo  =DecimalField(max_digits=20, decimal_places=2)
   
    def __str__(self) -> str:
        return self.conta





class Cartao(Model):

    usuario =ForeignKey(Usuario, on_delete=DO_NOTHING)
    nome  =CharField(max_length=60)
    numero_cartao =CharField(max_length=20)
    cvv =CharField(max_length=3)
    data_exp =DateField()

    def __str__(self) -> str:
        return self.id




class Fatura(Model):
    cartao = ForeignKey(Cartao, on_delete=CASCADE, verbose_name="Cartão")
    valor_fatura = DecimalField(max_digits=8, decimal_places=2)
    data_vencimento = DateField(verbose_name="Vencimento")
    data_pagamento = DateField(verbose_name="Pagamento")

    def __str__(self):
        return self.data_vencimento




class Transacao(Model):
    beneficiario = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Beneficiário", related_name='beneficiario')
    beneficiado = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Beneficiado", related_name='beneficiado')
    data_transacao = DateTimeField(verbose_name='Data', auto_now_add=True)
    valor_transacao = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return self.beneficiario + " " + self.beneficiado





class Emprestimo(Model):
    STATUS_DIA = 'D'
    STATUS_ATRASADO = 'A'

    STATUS = [(STATUS_DIA, 'Em dia'),(STATUS_ATRASADO, 'Em atraso'),]

    status = CharField(max_length=1, choices=STATUS, default=STATUS_DIA, verbose_name="Status")
    conta = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Conta")
    valor = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor do empréstimo")
    data = DateTimeField(verbose_name="Data", auto_now_add=True)
    juros = DecimalField(max_digits=4, decimal_places=2, verbose_name="Juros")
    parcelas = SmallIntegerField()

    def __str__(self):
        return str(self.conta)




class Pag_emprestimo(Model):

    emprestimo = ForeignKey(Emprestimo, on_delete=CASCADE, verbose_name="Emprestimo")
    data_vencimento = DateField(verbose_name="Data de vencimento")
    valor_parcela = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor da parcela")
    data_pagamento = DateField(verbose_name="Data de pagamento")

    def __str__(self):
        return str(self.emprestimo)




class Favoritos(Model):
    usuario = ForeignKey(Usuario, on_delete=CASCADE, verbose_name="Usuário", related_name="usuario")
    ctt_favorito = ForeignKey(Usuario, on_delete=CASCADE, verbose_name="Favorito", related_name="favorito")

    def __str__(self):
        return self.usuario



class Extrato(Model):
    OP_SAIDA = 'S'
    OP_ENTRADA = 'E'

    OPERACAO = [
        (OP_ENTRADA, 'Entrada'),
        (OP_SAIDA, 'Saída')
    ]

    conta = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Conta")
    operacao = CharField(max_length=1, choices=OPERACAO,default=OP_ENTRADA, verbose_name="Operação")
    data = DateTimeField(auto_now_add=True, verbose_name="Data")
    valor = DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return self.conta

