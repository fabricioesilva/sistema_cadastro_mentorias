# Generated by Django 4.2.3 on 2023-09-19 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assinaturas', '0020_alteracoestermos_termosdeuso_termosaceitos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termosdeuso',
            old_name='title',
            new_name='termo_title',
        ),
    ]
