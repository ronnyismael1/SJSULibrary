from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('home/', views.home),
    path('register/', views.register),
    path('login/', views.login),
]
