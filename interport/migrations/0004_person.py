# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interport', '0003_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=30, blank=True)),
                ('age', models.CharField(max_length=30, blank=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
