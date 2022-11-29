from django.db import models

class Usuario(models.Model):
    SEXO_MASCULINO = 'm'
    SEXO_FEMININO = 'f'

    SEXO_TIPOS = [
        (SEXO_MASCULINO, 'masculino'),
        (SEXO_FEMININO, 'feminino'),
    ]

    nome = models.CharField(max_length=125)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_TIPOS)
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.id

class Conta(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    agencia = models.CharField(max_length=5)
    conta  = models.CharField(max_length=8)
    saldo  = models.DecimalField(max_digits=20, decimal_places=2)
   
    def __str__(self) -> str:
        return self.conta

class Cartao(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    nome  = models.CharField(max_length=60)
    numero_cartao = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)
    data_exp = models.DateField()

    def __str__(self) -> str:
        return self.id