# Generated by Django 4.2.1 on 2023-06-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0058_alter_descontos_criado_por_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planosassinatura',
            name='criado_por_nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
