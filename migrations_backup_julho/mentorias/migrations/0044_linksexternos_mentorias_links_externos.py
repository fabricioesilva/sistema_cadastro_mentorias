# Generated by Django 4.2.1 on 2023-06-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorias', '0043_delete_arquivosmentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinksExternos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Titulo do link')),
                ('link_url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('descricao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='mentorias',
            name='links_externos',
            field=models.ManyToManyField(blank=True, to='mentorias.linksexternos'),
        ),
    ]
