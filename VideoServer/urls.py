from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tarif/', views.tarif, name='tarif'),
    path('voity/', views.voity, name='voity'),
    path('zamer/', views.zamer, name='zamer'),
    path('balans/', views.balans, name='balans'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
]

