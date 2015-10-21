# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quorahome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_answered',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date posted'),
        ),
    ]
