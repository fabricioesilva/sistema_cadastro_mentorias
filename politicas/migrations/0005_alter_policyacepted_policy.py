# Generated by Django 4.2.3 on 2023-09-19 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politicas', '0004_alter_aboutus_options_alter_devpolicyrules_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyacepted',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politicas.policyrules', verbose_name='Política de privacidade'),
        ),
    ]
