# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0002_auto_20151005_0023'),
        ('ftp_import', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTPCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('base_url', models.CharField(max_length=512)),
                ('base_directory', models.CharField(max_length=512)),
                ('imported', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField()),
                ('ftp', models.ForeignKey(to='ftp_import.FTPConnect')),
                ('gallery', models.ForeignKey(to='collections.Gallery')),
            ],
        ),
    ]
