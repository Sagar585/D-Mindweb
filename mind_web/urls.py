from django.contrib import admin
from django.urls import path
from mind_web import views

urlpatterns = [
    path('mindweb.vercel.app/reg_page',views.registration, name='reg_page'),
    path('mindweb.vercel.app/',views.loginPage, name='login_form'),
    path('mindweb.vercel.app/login',views.loginPage, name='login'),
    path('mindweb.vercel.app/home',views.home, name='home'),
    path('mindweb.vercel.app/contactus', views.contactus, name='contactus'),
    path('mindweb.vercel.app/alphabets', views.alphabets, name='alphabets'),
    path('mindweb.vercel.app/number_table', views.number_table, name='number_table'),
    path('mindweb.vercel.app/mathgame',views.mathgame, name='mathgame'),
    path('mindweb.vercel.app/ADD',views.ADD, name='add'),
    path('mindweb.vercel.app/subtract',views.subtract, name='subtract'),
    path('mindweb.vercel.app/multiply',views.multiply, name='multiply'),
    path('mindweb.vercel.app/divide',views.divide, name='divide'),
    path('mindweb.vercel.app/alpha-game',views.alphagame, name='alpha-game'),
    path('mindweb.vercel.app/alpha-song',views.alphasong, name='alpha-song'),
    path('mindweb.vercel.app/logout',views.LogoutPage,name='logout'),
]