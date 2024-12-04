from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    nome = models.CharField(max_length=50, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=12, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    carro = models.CharField(max_length=50, null=False, blank=False)
    placa = models.CharField(max_length=9, null=False, blank=False)
    ano = models.IntegerField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, default=1)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='servicos/', null=True, blank=True)

    def __str__(self) -> str:
        return self.carro

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cargo = models.CharField(max_length=100, null=False, blank=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f'Agendamento: {self.cliente} com {self.funcionario} em {self.data_hora}'
