# Generated by Django 4.2.1 on 2023-06-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0057_descontos_alter_mentorias_resumo_mentoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descontos',
            name='criado_por_nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
