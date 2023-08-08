# Generated by Django 4.0 on 2023-08-07 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0012_remove_simulados_pontuacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentoria',
            name='matriculas',
        ),
        migrations.AddField(
            model_name='matriculaalunomentoria',
            name='mentoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentorias.mentoria'),
        ),
    ]
