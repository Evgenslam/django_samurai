from django import template
from samurai.models import Category, PostTag

register = template.Library()

@register.inclusion_tag('samurai/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('samurai/list_tags.html')
def show_all_tags():
    return {'tags': PostTag.objects.all()}