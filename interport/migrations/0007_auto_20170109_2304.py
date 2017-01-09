# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interport', '0006_auto_20170109_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='username',
            new_name='name',
        ),
    ]
