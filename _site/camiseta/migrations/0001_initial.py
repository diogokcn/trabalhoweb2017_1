# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=20)),
                ('tamanho', models.CharField(max_length=10)),
                ('cor', models.CharField(max_length=10)),
                ('tecido', models.CharField(max_length=30)),
                ('preco', models.FloatField()),
            ],
        ),
    ]
