from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "addpage"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"}
]

samurai_list = [
    {"id": 1, "name": "Миямото Мусаси 宮本 武蔵", "content": "Легендарный фехтовальщик, известный своим непобежденным рекордом в поединках.", "is_published": True},
    {"id": 2, "name": "Ода Нобунага 織田 信長", "content": "Могущественный даймё, сыгравший важную роль в объединении Японии в конце периода Сэнгоку.", "is_published": True},
    {"id": 3, "name": "Токугава Иэясу 徳川 家康", "content": "Основатель и первый шогун Токугавского сёгуната, правившего Японией более 250 лет.", "is_published": True},
    {"id": 4, "name": "Датэ Масамунэ 伊達 政宗", "content": "Страшный и уважаемый даймё раннего периода Эдо, известный как 'Одноглазый дракон'.", "is_published": True},
    {"id": 5, "name": "Такэда Сингэн 武田 信玄", "content": "Известный даймё клана Такэда, известный своими военными тактикой и соперничеством с Уэсуги Кэнсином.", "is_published": False},
    {"id": 6, "name": "Уэсуги Кэнсин 上杉 謙信", "content": "Прославленный даймё клана Уэсуги, известный как 'Дракон Эчиго' за свои военные способности.", "is_published": False},
    {"id": 7, "name": "Хонда Тадакацу 本多 忠勝", "content": "Один из 'Четырех небесных королей' Токугавского сёгуната, прославленный своим мастерством на поле битвы и преданностью.", "is_published": False}
]

def index(request):
    data = {
        'title': 'лучшие самураи Татарстана',
        'menu': menu,
        'posts': samurai_list,
            }
    return render(request, "samurai/index.html", context=data)

def about(request):
    data = {'title': about.__name__}
    return render(request, "samurai/about.html", data)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Здесь будет форма обратной связи")

def login(request):
    return HttpResponse("Здесь будет логин")


def show_post(request, post_id):
    return HttpResponse(f"Подробная информация по id: {post_id}")

def page_not_found(reuequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



