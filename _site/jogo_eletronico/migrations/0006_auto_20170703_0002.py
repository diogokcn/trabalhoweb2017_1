# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_eletronico', '0005_auto_20170702_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogoeletronico',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'user'),
        ),
    ]
