# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
