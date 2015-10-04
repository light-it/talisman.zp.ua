# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='featured',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u043a\u0430\u0440\u0443\u0441\u0435\u043b\u0438'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043a\u0430\u0440\u0443\u0441\u0435\u043b\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_url',
            field=models.URLField(null=True, verbose_name='\u0421\u0441\u043b\u044b\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043a\u0430\u0440\u0443\u0441\u0435\u043b\u0438', blank=True),
        ),
    ]
