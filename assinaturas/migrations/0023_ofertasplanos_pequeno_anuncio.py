# Generated by Django 4.2.3 on 2023-09-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0022_rename_termos_title_alteracoestermos_termo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertasplanos',
            name='pequeno_anuncio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pequeno anúncio para a oferta'),
        ),
    ]
