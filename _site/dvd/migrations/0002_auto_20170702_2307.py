# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='ano',
            field=models.IntegerField(verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='duracao',
            field=models.IntegerField(verbose_name='Dura\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='genero',
            field=models.CharField(max_length=15, verbose_name='G\xeanero'),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='preco',
            field=models.FloatField(verbose_name='Pre\xe7o'),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='T\xedtulo'),
        ),
    ]
