# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0002_auto_20151005_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='category',
            field=models.ForeignKey(to='collections.Category', null=True),
        ),
    ]
