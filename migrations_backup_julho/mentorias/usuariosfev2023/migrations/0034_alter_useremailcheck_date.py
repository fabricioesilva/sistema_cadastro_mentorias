# Generated by Django 4.2.3 on 2024-01-20 22:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0033_alter_perfilcobranca_perfil_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailcheck',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data do email'),
        ),
    ]
