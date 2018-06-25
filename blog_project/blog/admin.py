from django.contrib import admin
from blog.models import *
# Register your models here.

#控制页面模块


class ArticleAdmin(admin.ModelAdmin):
    #     获取文本编辑器的js
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
        # 显示相应字段信息

    list_display = ('title', 'desc', 'content', 'click_count', 'date_publish', 'user', 'category',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('qq', 'mobile',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_publish', 'user', 'article', 'pid',)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'callback_url', 'date_publish', 'index',)


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url', 'callback_url', 'date_publish', 'index',)


# 为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Ad, AdAdmin)