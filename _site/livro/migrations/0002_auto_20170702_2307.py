# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano',
            field=models.IntegerField(verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autora',
            field=models.CharField(max_length=30, verbose_name='Autora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.CharField(max_length=20, verbose_name='Editora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='formato',
            field=models.CharField(max_length=20, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nroPags',
            field=models.IntegerField(verbose_name='Nro P\xe1ginas'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.FloatField(verbose_name='Pre\xe7o'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='T\xedtulo'),
        ),
    ]
