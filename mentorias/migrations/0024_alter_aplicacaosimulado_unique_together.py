# Generated by Django 4.0 on 2023-08-16 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0023_alter_arquivosmentoria_titulo_arquivo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='aplicacaosimulado',
            unique_together={('matricula', 'simulado')},
        ),
    ]
