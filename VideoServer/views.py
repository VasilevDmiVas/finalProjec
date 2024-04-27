from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('room'))
    else:
        return HttpResponseRedirect(reverse('room'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('room_list'))


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if not username or not email or not password or not confirm_password:

            return render(request, 'signup.html')


        if password != confirm_password:
            # return HttpResponseRedirect(reverse('signup'))
            return render(request, 'signup.html')


        user = User.objects.create_user(username, email, password)
        login(request, user)
        # return HttpResponseRedirect(reverse('home'))
        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
        # return HttpResponseRedirect(reverse('home'))




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