# Generated by Django 4.2.1 on 2023-07-16 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_rename_user_preferences_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Preferências do usuário'),
        ),
    ]
