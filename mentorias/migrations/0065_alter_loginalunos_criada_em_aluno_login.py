# Generated by Django 4.2.3 on 2024-02-12 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0064_loginalunos_email_aluno_login_original_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginalunos',
            name='criada_em_aluno_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 19, 17, 24, 344263), verbose_name='Criada em:'),
        ),
    ]
