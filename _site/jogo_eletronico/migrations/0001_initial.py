# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JogoEletronico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('estudio', models.CharField(max_length=20)),
                ('distribuidor', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=10)),
                ('ano', models.IntegerField()),
                ('preco', models.FloatField()),
            ],
        ),
    ]
