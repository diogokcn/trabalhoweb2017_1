# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_eletronico', '0003_auto_20170702_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogoeletronico',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
