# Generated by Django 4.0 on 2023-09-15 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0017_ofertasplanos_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='precosassinatura',
            name='condicoes',
            field=models.TextField(blank=True, null=True, verbose_name='Condições do plano em HTML'),
        ),
    ]