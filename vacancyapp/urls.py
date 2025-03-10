from django.urls import path
from .views import home, vacanciapp_list, vacancy_detail

urlpatterns = [
    path('',home, name='home_page'),
    path('vacanciapp/', vacanciapp_list, name='vacanciapp_list"),
    path('contact/', views.contact_page, name='contact_page'),
]
