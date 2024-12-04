# Generated by Django 5.1.1 on 2024-12-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
