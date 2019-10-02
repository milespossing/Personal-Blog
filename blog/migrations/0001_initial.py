# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-02 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
