# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jogo_eletronico', '0002_auto_20170626_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogoeletronico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='ano',
            field=models.IntegerField(verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='distribuidor',
            field=models.CharField(max_length=20, verbose_name='Distribuidor'),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='estudio',
            field=models.CharField(max_length=20, verbose_name='Est\xfadio'),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='genero',
            field=models.CharField(max_length=20, verbose_name='G\xeanero'),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='preco',
            field=models.FloatField(verbose_name='Pre\xe7o'),
        ),
        migrations.AlterField(
            model_name='jogoeletronico',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='T\xedtulo'),
        ),
    ]
