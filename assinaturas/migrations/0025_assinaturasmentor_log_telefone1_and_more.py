# Generated by Django 4.2.3 on 2023-09-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0024_rename_preco_ofetado_ofertasplanos_preco_ofertado'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_telefone1',
            field=models.CharField(max_length=25, null=True, verbose_name='Telefone de contato com o DDD*'),
        ),
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_telefone2',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Outro telefone de contato com o DDD'),
        ),
    ]
