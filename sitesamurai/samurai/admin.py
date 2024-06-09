from django.contrib import admin
from .models import Samurai, Category, Lifework, PostTag

admin.site.register(
    [
        Samurai,
        Category,
        Lifework,
        PostTag,
    ]
)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Самураи разных мастей"
