# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('editora', models.CharField(max_length=20)),
                ('autora', models.CharField(max_length=30)),
                ('nroPags', models.IntegerField()),
                ('formato', models.CharField(max_length=20)),
                ('preco', models.FloatField()),
            ],
        ),
    ]
