from django.contrib import admin

from .models import Category, Lifework, PostTag, Samurai


@admin.register(Samurai)
class SamuraiAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "time_create", "is_published", "category"]
    list_display_links = ["id", "name"]
    ordering = ["-time_create", "name"]
    list_editable = ["is_published", "category"]
    list_per_page = 15


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    ordering = ["name"]


@admin.register(Lifework)
class LifeworkAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    ordering = ["name"]


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ["id", "tag"]
    list_display_links = ["id", "tag"]
    ordering = ["tag"]


admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Самураи разных мастей"
