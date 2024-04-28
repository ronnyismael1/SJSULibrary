from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('home/', views.home, name='home'),
    path('reports/', views.reports, name='reports'),
]
