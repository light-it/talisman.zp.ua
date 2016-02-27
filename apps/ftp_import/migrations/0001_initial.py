# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FTPConnect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('host', models.CharField(max_length=512)),
                ('login', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=1024)),
            ],
        ),
    ]
