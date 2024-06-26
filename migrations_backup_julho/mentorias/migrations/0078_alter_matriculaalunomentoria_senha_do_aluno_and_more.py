# Generated by Django 4.2.1 on 2023-07-25 01:16

from django.db import migrations, models
import mentorias.models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0077_alter_aplicacaosimulado_senha_do_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculaalunomentoria',
            name='senha_do_aluno',
            field=models.TextField(blank=True, default=mentorias.models.get_random_string, null=True, verbose_name='Senha para acesso'),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='mentor_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='mentor_username',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='titulo',
            field=models.TextField(verbose_name='Título do simulado'),
        ),
    ]
