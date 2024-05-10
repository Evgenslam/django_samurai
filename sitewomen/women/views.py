from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
            }
    return render(request, "women/index.html", context=data)

def about(request):
    data = {'title': about.__name__}
    return render(request, "women/about.html", data)

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(reuequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



