from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Category, PostTag, Samurai

menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "addpage"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"}
]


def index(request):
    samurai_info = Samurai.published.all()
    data = {
        'title': 'лучшие самураи по итогам 2023',
        'menu': menu,
        'posts': samurai_info,
        'cat_selected': 0,
            }
    return render(request, "samurai/index.html", context=data)


def about(request):
    data = {'title': about.__name__}
    return render(request, "samurai/about.html", context={'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Здесь будет форма обратной связи")


def login(request):
    return HttpResponse("Здесь будет логин")


def show_post(request, post_slug):
    post = get_object_or_404(Samurai, slug=post_slug)
    data = {
        'title': post.name,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'samurai/post.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Samurai.published.filter(category=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, "samurai/index.html", context=data)


def page_not_found(reuequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_tag(request, tag_slug):
    tag = get_object_or_404(PostTag, slug=tag_slug)
    posts = tag.samurais.filter(is_published=Samurai.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, "samurai/index.html", context=data)
