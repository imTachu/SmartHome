# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructorCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('fixed_phone', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)])),
                ('fixed_phone_extension', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('contact_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'date')),
                ('description', models.CharField(max_length=200)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('type', models.CharField(max_length=30, choices=[(b'0', b'Disparo de alarma'), (b'1', b'Activar alarma'), (b'3', b'Alerta en sensor'), (b'2', b'Desactivar alarma'), (b'4', b'Cambio actuador')])),
                ('is_critical', models.BooleanField(default=False)),
                ('is_fatal', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=100, null=True)),
                ('fixed_phone', models.CharField(max_length=15, null=True)),
                ('plan', models.CharField(max_length=300, null=True)),
                ('is_secure_mode', models.BooleanField(default=True)),
                ('constructor_company', models.ForeignKey(to='watchapp.ConstructorCompany', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=30, choices=[(b'0', b'Sensor'), (b'1', b'Actuador')])),
                ('location_in_plan', models.CharField(max_length=20, null=True)),
                ('is_discrete', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=30, choices=[(b'0', b'Sensor'), (b'1', b'Actuador')])),
                ('property', models.ForeignKey(to='watchapp.Property', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('properties_as_owner', models.ManyToManyField(related_name='properties_as_owner', to='watchapp.Property')),
                ('properties_as_resident', models.ManyToManyField(related_name='properties_as_resident', to='watchapp.Property')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='property',
            field=models.ForeignKey(to='watchapp.Property'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='sensor',
            field=models.ForeignKey(to='watchapp.Sensor'),
            preserve_default=True,
        ),
    ]
