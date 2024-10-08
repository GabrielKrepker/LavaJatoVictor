from django.db import models
from clientes.models import Cliente
from .choices import ChoicesTipoServico
from datetime import datetime
from secrets import token_hex, token_urlsafe

class TipoServico(models.Model):
    titulo = models.CharField(max_length=50, choices=ChoicesTipoServico.choices, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=30, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    tipo_servico = models.ManyToManyField(TipoServico)
    data_inicio = models.DateField(null=True, blank=True)
    data_entrega = models.DateField(null=True, blank=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.cliente.nome if self.cliente else 'Sem Cliente'}"

    def preco_total(self):
        preco_total = float(0)
        for tipo in self.tipo_servico.all():
            preco_total += float(tipo.preco)
        return preco_total