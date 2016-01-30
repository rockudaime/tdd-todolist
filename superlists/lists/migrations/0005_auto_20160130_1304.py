# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20160130_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='lists.List'),
            preserve_default=True,
        ),
    ]
