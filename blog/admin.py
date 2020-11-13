from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Tags, Category


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'created_time',)
#     list_display_links = ('title',)


# admin.site.register(Article, ArticleAdmin)  # 向admin注册这个model
admin.site.register(Tags)
admin.site.register(Article)
admin.site.register(Category)

admin.site.site_title = '才智小天地'
admin.site.site_header = '才智小天地'