# Generated by Django 4.2.3 on 2024-02-13 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0066_alter_loginalunos_criada_em_aluno_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginalunos',
            name='criada_em_aluno_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criada em:'),
        ),
    ]
