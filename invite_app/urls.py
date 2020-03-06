from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.reg),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('invite1', views.invite1),
    path('invite2', views.invite2),
    path('invite3', views.invite3),
    path('profile', views.profile),
    path('about', views.about),
    path('contact', views.contact),
    path('accept_invite', views.acceptInvite),
]