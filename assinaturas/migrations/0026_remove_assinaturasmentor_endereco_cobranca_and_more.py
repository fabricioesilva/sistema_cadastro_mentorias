# Generated by Django 4.2.3 on 2023-09-22 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0033_alter_perfilcobranca_perfil_pagamento'),
        ('assinaturas', '0025_assinaturasmentor_log_telefone1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assinaturasmentor',
            name='endereco_cobranca',
        ),
        migrations.AddField(
            model_name='assinaturasmentor',
            name='perfil_cobranca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.perfilcobranca', verbose_name='Perfil de cobrança'),
        ),
    ]