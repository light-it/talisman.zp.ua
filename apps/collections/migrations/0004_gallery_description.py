# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0003_auto_20160227_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
