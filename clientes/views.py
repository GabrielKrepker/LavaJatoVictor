from django.shortcuts import render
from django.utils.timezone import now, make_aware, get_current_timezone
from datetime import datetime
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

        if data_hora:
            from datetime import datetime
            data_hora_obj = datetime.fromisoformat(data_hora)
            data_hora_obj = make_aware(data_hora_obj, get_current_timezone())

            if data_hora_obj < now():
                return render(request, 'clientes/agendar.html', {
                    'clientes': clientes,
                    'funcionarios': funcionarios,
                    'error': 'Não é possível agendar para uma data anterior à atual.',
                    'cliente_selecionado': cliente_id,
                    'funcionario_selecionado': funcionario_id,
                    'data_hora': data_hora,
                })

        Agendamento.objects.create(
            cliente_id=cliente_id,
            funcionario_id=funcionario_id,
            data_hora=data_hora_obj
        )

        return render(request, 'clientes/agendar.html', {
            'clientes': clientes,
            'funcionarios': funcionarios,
            'success': 'Agendamento realizado com sucesso!',
            'cliente_selecionado': '',
            'funcionario_selecionado': '',
            'data_hora': '',
        })

    return render(request, 'clientes/agendar.html', {
        'clientes': clientes,
        'funcionarios': funcionarios,
        'cliente_selecionado': '',
        'funcionario_selecionado': '',
        'data_hora': '',
    })

def servicos(request):
    realizados = Agendamento.objects.filter(data_hora__lt=now())
    futuros = Agendamento.objects.filter(data_hora__gte=now())

    if request.method == 'POST':
        agendamento_id = request.POST.get('agendamento_id')
        concluido = request.POST.get('concluido') == 'on'
        Agendamento.objects.filter(id=agendamento_id).update(concluido=concluido)

    return render(request, 'clientes/servicos.html', {
        'realizados': realizados,
        'futuros': futuros
    })
