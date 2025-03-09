from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h4>Это главная страница</h4>")

def about_page(request):
    return HttpResponse("<h4>О нас</h4>")

def contact_page(request):
    return HttpResponse("<h4>Контакты</h4>")