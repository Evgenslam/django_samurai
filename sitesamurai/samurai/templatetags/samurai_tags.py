from django import template
from django.db.models import Count
from samurai.models import Category, PostTag

register = template.Library()


@register.inclusion_tag('samurai/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('samurais')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('samurai/list_tags.html')
def show_all_tags():
    return {'tags': PostTag.objects.annotate(total=Count('samurais')).filter(total__gt=0)}
