# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0003_remove_sensor_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='property',
            field=models.ForeignKey(to='watchapp.Property', null=True),
            preserve_default=True,
        ),
    ]
