# Generated by Django 4.1.1 on 2025-01-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='categoria_manutencao',
            field=models.CharField(choices=[('TVM', 'Trocar válvula do motor'), ('TO', 'Troca de óleo'), ('BAL', 'Balanceamento')], default='TVM', max_length=3),
        ),
    ]
