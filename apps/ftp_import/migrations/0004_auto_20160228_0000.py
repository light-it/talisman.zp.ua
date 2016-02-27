# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_import', '0003_auto_20160227_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftpcollection',
            name='base_url',
            field=models.URLField(),
        ),
    ]
