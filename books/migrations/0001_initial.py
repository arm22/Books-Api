# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('pdate', models.CharField(max_length=200)),
                ('pname', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('sum', models.CharField(max_length=1000)),
                ('url', models.URLField(max_length=100)),
                ('img', models.URLField(max_length=100)),
            ],
        ),
    ]
