# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=30, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default='avatar/default.png', upload_to='avatar/%Y/%m', null=True, blank=True, max_length=200, verbose_name='用户头像')),
                ('qq', models.CharField(blank=True, null=True, verbose_name='QQ号码', max_length=20)),
                ('mobile', models.CharField(unique=True, blank=True, null=True, verbose_name='手机号码', max_length=11)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', blank=True, to='auth.Group', related_name='user_set', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_query_name='user', blank=True, to='auth.Permission', related_name='user_set', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户',
                'ordering': ['-id'],
                'verbose_name': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='广告标题')),
                ('description', models.CharField(max_length=200, verbose_name='广告描述')),
                ('image_url', models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')),
                ('callback_url', models.URLField(blank=True, null=True, verbose_name='回调url')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('index', models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')),
            ],
            options={
                'verbose_name_plural': '广告',
                'ordering': ['index', 'id'],
                'verbose_name': '广告',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=50, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_count', models.IntegerField(default=0, verbose_name='点击次数')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-date_publish'],
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='显示顺序(从小到大)')),
            ],
            options={
                'verbose_name_plural': '分类',
                'ordering': ['index', 'id'],
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('article', models.ForeignKey(null=True, blank=True, to='blog.Article', verbose_name='文章')),
                ('pid', models.ForeignKey(null=True, blank=True, to='blog.Comment', verbose_name='父级评论')),
                ('user', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '评论',
                'ordering': ['-date_publish'],
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('description', models.CharField(max_length=200, verbose_name='友情链接描述')),
                ('callback_url', models.URLField(verbose_name='url地址')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('index', models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')),
            ],
            options={
                'verbose_name_plural': '友情链接',
                'ordering': ['index', 'id'],
                'verbose_name': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'ordering': ['id'],
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
