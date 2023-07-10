# Generated by Django 4.2.1 on 2023-07-09 21:53

from django.db import migrations, models
import django.db.models.deletion
import mentorias.models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0064_aplicacaosimulado_matricula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculaalunomentoria',
            name='senha_do_aluno',
            field=models.CharField(blank=True, default=mentorias.models.get_random_string, max_length=6, null=True, verbose_name='Senha para acesso'),
        ),
        migrations.AlterField(
            model_name='aplicacaosimulado',
            name='matricula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aplicacoes_matricula', to='mentorias.matriculaalunomentoria'),
        ),
    ]
