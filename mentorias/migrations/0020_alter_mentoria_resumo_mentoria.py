# Generated by Django 4.0 on 2023-08-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0019_remove_mentoria_arquivos_da_mentoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentoria',
            name='resumo_mentoria',
            field=models.TextField(blank=True, help_text='Se desejar, escreva um texto de apresentação desta mentoria ao estudante.', null=True, verbose_name='Apresentação da mentoria'),
        ),
    ]
