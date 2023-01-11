from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'anons', 'date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'full_text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'date')

admin.site.register(Articles, ArticlesAdmin)
# Register your models here.
