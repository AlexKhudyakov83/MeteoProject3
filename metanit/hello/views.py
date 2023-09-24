from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h3>О сайте</h3>")


def contact(request):
    return HttpResponse("<h1>Контакты</h1>")


