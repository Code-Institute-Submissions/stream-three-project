# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(choices=[('M', 'Stretched and Mounted'), ('U', 'Stretched and Unmounted')], default=1, max_length=1)),
            ],
        ),
    ]