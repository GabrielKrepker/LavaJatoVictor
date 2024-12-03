from django.shortcuts import render, redirect
from .models import Agendamento, Cliente, Funcionario

def home(request):
    return render(request, 'clientes/home.html')

def agendar(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        funcionario_id = request.POST.get('funcionario')
        data_hora = request.POST.get('data_hora')

        Agendamento.objects.create(
            cliente_id=cliente_id, 
            funcionario_id=funcionario_id, 
            data_hora=data_hora
        )
        return render(request, 'clientes/agendar.html', {
            'clientes': clientes,
            'funcionarios': funcionarios,
            'success': 'Agendamento realizado com sucesso!'
        })
    
    return render(request, 'clientes/agendar.html', {
        'clientes': clientes,
        'funcionarios': funcionarios,
    })

def servicos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'clientes/servicos.html', {
        'agendamentos': agendamentos
    })