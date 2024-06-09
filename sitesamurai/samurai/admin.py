from django.contrib import admin
from .models import Samurai, Category, Lifework, PostTag

@admin.register(Samurai)
class SamuraiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_create', 'is_published']
    list_display_links = ['id', 'name']
    ordering = ['-time_create', 'name']

admin.site.register(
    [
        Category,
        Lifework,
        PostTag,
    ]
)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Самураи разных мастей"
