# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camiseta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camiseta',
            name='cor',
            field=models.CharField(max_length=10, verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='camiseta',
            name='marca',
            field=models.CharField(max_length=20, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='camiseta',
            name='preco',
            field=models.FloatField(verbose_name='Pre\xe7o'),
        ),
        migrations.AlterField(
            model_name='camiseta',
            name='tamanho',
            field=models.CharField(max_length=10, verbose_name='Tamanho'),
        ),
        migrations.AlterField(
            model_name='camiseta',
            name='tecido',
            field=models.CharField(max_length=30, verbose_name='Tecido'),
        ),
    ]
