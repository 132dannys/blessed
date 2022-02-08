from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['hello', 'world', '132']

    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
