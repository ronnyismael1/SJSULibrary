from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('home/', views.home, name='home'),
    path('books/', views.books, name='books'),

    path('checkout/', views.checkout, name='checkout'),
    path('addNew/', views.addNew, name='addNew'),
    
    path('reports/', views.reports, name='reports'),
    path('addLibrarian/', views.addLibrarian, name='addLibrarian'),
]
