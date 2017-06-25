# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=15)),
                ('ano', models.IntegerField()),
                ('duracao', models.IntegerField()),
                ('preco', models.FloatField()),
            ],
        ),
    ]
