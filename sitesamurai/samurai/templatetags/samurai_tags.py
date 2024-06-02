from django import template
import samurai.views as views
from samurai.models import Category

@register.inclusion_tag('samurai/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
