from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# try:
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Страница в разработке')
        else:
            return HttpResponse('Пользователь не найден либо пароль неверен')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not username or not email or not password or not confirm_password:
                return HttpResponse('Не все поля заполнены повторите попытку')

            if password != confirm_password:
                return HttpResponse('Пароли не совпадают повторите попытку')

            user = User.objects.create_user(username, email, password)
            login(request, user)
            return HttpResponse('Страница в разработке')
        else:
            return render(request, 'signup.html')
    except:
        return HttpResponse('Имя пользователя занято повторите попытку')


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
