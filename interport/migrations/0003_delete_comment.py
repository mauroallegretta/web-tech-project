# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interport', '0002_auto_20170109_1735'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
