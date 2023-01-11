from django.http import HttpResponseNotFound
from django.shortcuts import render

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Документы', 'url_name': 'docs_home'},
        {'title': 'Про нас', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'about'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Регистрация на портале', 'url_name': 'login'},]

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'Про нас'
    }
    return render(request, 'main/about.html', data)

def contacts(request):
    data = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')

