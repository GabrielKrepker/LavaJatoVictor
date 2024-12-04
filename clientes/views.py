from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, make_aware, get_current_timezone
from datetime import datetime
from .models import Agendamento, Cliente, Funcionario

def home(request):
    return render(request, 'clientes/home.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            cliente = Cliente.objects.get(user__email=email)
        except Cliente.DoesNotExist:
            return render(request, 'clientes/home.html', {'error': 'Usuário não encontrado.'})

        if password != cliente.cpf:
            return render(request, 'clientes/home.html', {'error': 'CPF incorreto.'})

        user = authenticate(request, username=cliente.user.username, password=password)

        if user:
            login(request, user)
            return redirect('agendar')
        else:
            return render(request, 'clientes/home.html', {'error': 'Erro de autenticação, CPF incorreto.'})

    return render(request, 'clientes/home.html')

def register_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        if Cliente.objects.filter(cpf=cpf).exists():
            return render(request, 'clientes/home.html', {'error': 'CPF já cadastrado.'})

        if User.objects.filter(username=nome).exists():
            return render(request, 'clientes/home.html', {'error': 'Usuário já existe.'})

        user = User.objects.create_user(username=nome, email=email, password=cpf)

        Cliente.objects.create(
            user=user,
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )

        login(request, user)
        return redirect('agendar')

    return render(request, 'clientes/home.html')

@login_required
def agendar(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()

    cliente = Cliente.objects.get(user=request.user)
    usuario_nome = cliente.nome

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        funcionario_id = request.POST.get('funcionario')
        data_hora = request.POST.get('data_hora')

        if data_hora:
            data_hora_obj = make_aware(datetime.fromisoformat(data_hora), get_current_timezone())
            if data_hora_obj < now():
                return render(request, 'clientes/agendar.html', {
                    'clientes': clientes,
                    'funcionarios': funcionarios,
                    'error': 'Não é possível agendar para uma data anterior à atual.',
                    'cliente_selecionado': cliente_id,
                    'funcionario_selecionado': funcionario_id,
                    'data_hora': data_hora,
                    'usuario_nome': usuario_nome 
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
            'usuario_nome': usuario_nome,
            'cliente_selecionado': '',
            'funcionario_selecionado': '',
            'data_hora': '',
        })

    return render(request, 'clientes/agendar.html', {
        'clientes': clientes,
        'funcionarios': funcionarios,
        'usuario_nome': usuario_nome
    })

@login_required
def servicos(request):
    cliente = Cliente.objects.get(user=request.user)
    usuario_nome = cliente.nome
    
    realizados = Agendamento.objects.filter(data_hora__lt=now())
    futuros = Agendamento.objects.filter(data_hora__gte=now())

    if request.method == 'POST':
        agendamento_id = request.POST.get('agendamento_id')
        concluido = request.POST.get('concluido') == 'on'
        
        Agendamento.objects.filter(id=agendamento_id).update(concluido=concluido)

    return render(request, 'clientes/servicos.html', {
        'realizados': realizados,
        'futuros': futuros,
        'usuario_nome': usuario_nome
    })

def logout_user(request):
    logout(request)
    return redirect('home')
