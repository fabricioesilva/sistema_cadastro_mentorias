# Generated by Django 4.2.1 on 2023-05-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0014_alter_alunos_turma_matriculada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='arquivos_aluno',
            field=models.ManyToManyField(blank=True, help_text='Arquivos de um Aluno são arquivos disponíveis ao estudante selecionado.', to='mentorias.arquivosaluno'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='email_aluno',
            field=models.EmailField(help_text='Este email precisa bater com o email utilizado pelo estudante para se cadastrar.', max_length=254, verbose_name='Email do Aluno'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='nivel_preparo',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Iniciante'), (2, 'Intermediário'), (3, 'Avançado')], default=1, null=True, verbose_name='Nível de preparo para o objetivo final.'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='simulados_realizados',
            field=models.ManyToManyField(blank=True, help_text='Simulados que os alunos devem fazer.', to='mentorias.simulados'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='turma_matriculada',
            field=models.ManyToManyField(blank=True, to='mentorias.turmas', verbose_name='Turma matriculada'),
        ),
    ]
