# Generated by Django 5.1.1 on 2024-12-04 02:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=9)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('lavagens', models.IntegerField(default=0)),
                ('consertos', models.IntegerField(default=0)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='servicos/')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('concluido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.funcionario')),
            ],
        ),
    ]
