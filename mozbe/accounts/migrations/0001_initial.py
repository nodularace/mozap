# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('language', models.CharField(max_length=30, unique=True)),
                ('currency', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]