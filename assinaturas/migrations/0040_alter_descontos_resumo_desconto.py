# Generated by Django 4.2.3 on 2024-02-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0039_remove_descontos_abreviatura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descontos',
            name='resumo_desconto',
            field=models.CharField(blank=True, help_text='Escreva um resumo de até 100 caracteres.', max_length=100, null=True, verbose_name='Resumo do desconto'),
        ),
    ]
