# Generated by Django 4.0 on 2023-08-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0009_simulados_estatisticas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulados',
            name='questao_tipo',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'ABCD'), (2, 'ABCDE'), (3, 'Certo/Errado')], default=2, null=True, verbose_name='Tipo de questões'),
        ),
    ]
