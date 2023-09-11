# Generated by Django 4.0 on 2023-09-10 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assinaturasmentor',
            name='limite_matriculas',
        ),
        migrations.RemoveField(
            model_name='assinaturasmentor',
            name='meses_desconto_restante',
        ),
        migrations.RemoveField(
            model_name='assinaturasmentor',
            name='meses_isencao_restante',
        ),
        migrations.RemoveField(
            model_name='precosassinatura',
            name='preco',
        ),
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_meses_desconto_restante',
            field=models.IntegerField(blank=True, null=True, verbose_name='Meses com desconto'),
        ),
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_meses_isencao_restante',
            field=models.IntegerField(blank=True, null=True, verbose_name='Meses com isencao'),
        ),
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_percentual_desconto',
            field=models.FloatField(blank=True, null=True, verbose_name='Percentual de desconto contratado'),
        ),
    ]
