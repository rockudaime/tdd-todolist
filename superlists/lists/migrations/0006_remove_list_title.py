# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20160130_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='title',
        ),
    ]
