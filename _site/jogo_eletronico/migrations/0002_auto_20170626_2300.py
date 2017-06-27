# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_eletronico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogoeletronico',
            name='genero',
            field=models.CharField(max_length=20),
        ),
    ]
