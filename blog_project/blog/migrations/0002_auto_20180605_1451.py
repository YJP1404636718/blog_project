# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(verbose_name='邮箱地址', blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(verbose_name='个人网页地址', blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(verbose_name='用户名', blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(verbose_name='个人网页地址', blank=True, max_length=100, null=True),
        ),
    ]
