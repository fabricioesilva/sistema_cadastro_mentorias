# Generated by Django 4.2.1 on 2023-05-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0015_alter_alunos_arquivos_aluno_alter_alunos_email_aluno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorias',
            old_name='created',
            new_name='data_cadastro',
        ),
    ]
