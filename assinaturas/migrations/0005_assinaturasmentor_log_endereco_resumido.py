# Generated by Django 4.0 on 2023-09-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0004_remove_assinaturasmentor_usuario_endereco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinaturasmentor',
            name='log_endereco_resumido',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço resumido'),
        ),
    ]
