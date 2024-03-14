from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def tarif(request):
    return HttpResponse('Страница в разработке')


def voity(request):
    return HttpResponse('Страница в разработке')


def zamer(request):
    return HttpResponse('Страница в разработке')


def balans(request):
    return HttpResponse('Страница в разработке')


def shop(request):
    return HttpResponse('Страница в разработке')