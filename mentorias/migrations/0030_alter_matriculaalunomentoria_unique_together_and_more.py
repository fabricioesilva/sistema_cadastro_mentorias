# Generated by Django 4.2.1 on 2023-05-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0029_alter_matriculaalunomentoria_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matriculaalunomentoria',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='mentorias',
            name='matriculas',
            field=models.ManyToManyField(blank=True, null=True, to='mentorias.matriculaalunomentoria'),
        ),
        migrations.RemoveField(
            model_name='matriculaalunomentoria',
            name='mentoria',
        ),
    ]