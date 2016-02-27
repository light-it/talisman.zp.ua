# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_import', '0002_ftpcollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftpcollection',
            name='gallery',
            field=models.ForeignKey(to='collections.Gallery', null=True),
        ),
        migrations.AlterField(
            model_name='ftpcollection',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),
    ]
