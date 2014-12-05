# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='bar',
            field=models.CharField(default='blam!', max_length=200),
            preserve_default=False,
        ),
    ]
