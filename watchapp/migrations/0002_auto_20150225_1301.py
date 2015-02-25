# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructorcompany',
            name='user',
            field=models.OneToOneField(default=3, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='constructorcompany',
            name='fixed_phone',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='constructorcompany',
            name='fixed_phone_extension',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='constructorcompany',
            name='mobile_number',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='fixed_phone',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='plan',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
    ]
