from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('meta_keywords', 'title', 'is_published', 'created')
    ordering = ('-created', )
    list_filter = ('is_published', 'created')
    search_fields = ('title', )

admin.site.register(Article, ArticleAdmin)