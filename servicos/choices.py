from django.db import models

class ChoicesTipoServico(models.TextChoices):
    MANUTENCAO = 'MAN', 'Manutenção'
    REPARO = 'REP', 'Reparo'
    LIMPEZA = 'LIM', 'Limpeza'