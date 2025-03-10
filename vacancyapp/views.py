from django.shortcuts import render, get_object_or_404
from .model import Vacancy

def home(request):
    return render(request, 'home.html')

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "post_list.html", {"vacancies"}):

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    
