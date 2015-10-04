# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'256', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u0413\u043e\u0434')),
                ('name', models.CharField(max_length=b'256', verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', blank=True)),
                ('image_small', models.ImageField(upload_to=b'', null=True, verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', blank=True)),
                ('image_url', models.URLField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044e', blank=True)),
                ('image_small_url', models.URLField(null=True, verbose_name='\u0421\u043b\u043b\u044b\u043a\u0430 \u043d\u0430 \u043f\u0440\u0435\u0432\u044c\u044e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438', blank=True)),
                ('title', models.CharField(max_length=b'256', null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('model', models.CharField(max_length=b'256', null=True, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c', blank=True)),
                ('price', models.DecimalField(null=True, verbose_name='\u0426\u0435\u043d\u0430', max_digits=10, decimal_places=2, blank=True)),
                ('sex', models.CharField(blank=True, max_length=b'256', null=True, verbose_name='\u041f\u043e\u043b', choices=[(b'm', '\u041c\u0443\u0436\u0441\u043a\u0438\u0435'), (b'w', '\u0416\u0435\u043d\u0441\u043a\u0438\u0435')])),
                ('recommended', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='collections.Category')),
                ('gallery', models.ForeignKey(to='collections.Gallery')),
            ],
        ),
    ]
