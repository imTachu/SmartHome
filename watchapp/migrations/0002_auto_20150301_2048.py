# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='value',
            field=models.DecimalField(max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
