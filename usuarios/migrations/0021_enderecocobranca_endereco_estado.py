# Generated by Django 4.0 on 2023-09-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_enderecocobranca'),
    ]

    operations = [
        migrations.AddField(
            model_name='enderecocobranca',
            name='endereco_estado',
            field=models.CharField(default='MG', max_length=2, verbose_name='Estado'),
        ),
    ]
