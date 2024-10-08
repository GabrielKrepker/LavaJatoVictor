from django.contrib import admin
from .models import Cliente, Carro, Funcionario, Agendamento

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Funcionario)
admin.site.register(Agendamento)