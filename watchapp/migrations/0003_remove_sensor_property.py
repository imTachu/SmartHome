# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0002_auto_20150309_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='property',
        ),
    ]
