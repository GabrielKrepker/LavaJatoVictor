from django.contrib import admin
from .models import Cliente, Carro, Funcionario, Agendamento

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'cpf')
    search_fields = ('nome', 'sobrenome', 'email', 'cpf')

class CarroAdmin(admin.ModelAdmin):
    list_display = ('carro', 'placa', 'ano', 'cliente', 'lavagens', 'consertos')
    search_fields = ('carro', 'placa')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario')
    search_fields = ('nome', 'cargo')

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'funcionario', 'data_hora', 'concluido')
    search_fields = ('cliente__nome', 'funcionario__nome')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
