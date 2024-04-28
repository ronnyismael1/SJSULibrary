from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

@login_required(login_url='login')
@allowed_users(['admin', 'librarian', 'student'])
def home(request):
    return render(request, 'access_control/home.html')

@login_required(login_url='login')
@admin_only
def reports(request):
    return render(request, 'access_control/reports.html')

@unauthenticated_user
def registerPage(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='student')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'access_control/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'access_control/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def your_view(request):
    user = request.user
    is_librarian = user.groups.filter(name='librarian').exists()
    is_admin = user.groups.filter(name='admin').exists()

    context = {
        'is_librarian': is_librarian,
        'is_admin': is_admin,
        # other context variables
    }
    return render(request, 'navbar.html', context)
