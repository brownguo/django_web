from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time',)
    list_display_links = ('title',)


admin.site.register(Article, ArticleAdmin) # 像admin注册这个model
admin.site.site_title = 'dadada'
admin.site.site_header = 'dadada'