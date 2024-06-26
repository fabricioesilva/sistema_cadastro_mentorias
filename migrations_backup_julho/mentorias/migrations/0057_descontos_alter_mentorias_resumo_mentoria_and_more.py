# Generated by Django 4.2.1 on 2023-06-11 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentorias', '0056_alter_mentorias_resumo_mentoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Nome comercial do desconto')),
                ('abreviatura', models.CharField(blank=True, max_length=20, null=True, verbose_name='Abreviatura')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('criado_por_pk', models.PositiveIntegerField(blank=True, null=True)),
                ('criado_por_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('criado_por_nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=False, verbose_name='Em uso')),
                ('desconto', models.FloatField(default=0)),
                ('prazo_duracao', models.PositiveIntegerField(blank=True, null=True, verbose_name='Dias duração do desconto')),
                ('encerramento', models.DateTimeField(blank=True, null=True, verbose_name='Encerramento')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
            ],
        ),
        migrations.AlterField(
            model_name='mentorias',
            name='resumo_mentoria',
            field=models.TextField(blank=True, help_text='Se desejar, escreva um texto de apresentação desta mentoria ao estudante.', max_length=300, null=True, verbose_name='Resumo'),
        ),
        migrations.CreateModel(
            name='PlanosAssinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Nome comercial')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('criado_por_pk', models.PositiveIntegerField(blank=True, null=True)),
                ('criado_por_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('criado_por_nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=False, verbose_name='Em uso')),
                ('preco', models.FloatField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('desconto', models.ManyToManyField(to='mentorias.descontos')),
            ],
        ),
        migrations.CreateModel(
            name='AssinaturasMentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criada_em', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data assinatura')),
                ('encerra_em', models.DateField(blank=True, null=True, verbose_name='Encerra em')),
                ('pagamento', models.JSONField(blank=True, null=True, verbose_name='Controle de pagamentos')),
                ('usuario_pk', models.PositiveIntegerField(blank=True, null=True, verbose_name='Id do usuário')),
                ('usuario_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email do usuário')),
                ('usuario_nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do usuário')),
                ('desconto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentorias.descontos')),
                ('plano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentorias.planosassinatura', verbose_name='Plano de assinatura')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
